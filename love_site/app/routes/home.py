"""
Main routes for the love_site application.

This module defines Flask endpoints for the user interface,
handling form display and rendering of personalized messages.
"""

import os
import re
import tempfile
from flask import Blueprint, render_template, request, flash, send_file, url_for
from moviepy import TextClip, concatenate_videoclips, AudioFileClip
from werkzeug.utils import secure_filename

from ..services.messages import load_messages, personalize_messages

# Blueprint for home page routes
home_bp = Blueprint("home", __name__)


def validate_name(name, field_name):
    """
    Validate a user-entered name.

    Args:
        name (str): The name to validate.
        field_name (str): Field name for error messages.

    Returns:
        tuple: (validated_name, errors)
    """
    errors = []

    # Remove whitespace and limit length
    name = name.strip()[:50]  # Max 50 characters

    if not name:
        return "", errors  # Empty allowed for lover_name

    # Validate characters: letters, spaces, apostrophes, hyphens
    if not re.match(r"^[a-zA-ZÀ-ÿ\s'-]+$", name):
        errors.append(f"The {field_name} contains invalid characters.")

    # Check minimum length (if not empty)
    if len(name) < 2:
        errors.append(f"The {field_name} must contain at least 2 characters.")

    return name, errors


@home_bp.route("/", methods=["GET", "POST"])
def index():
    """
    Main application route.

    Handles form submission for personalization and video generation.

    Returns:
        Response: Rendered template with messages and optional video download.
    """
    lover_name = "bae"
    sender_name = "Djochrist"
    messages = []
    video_url = None

    if request.method == "POST":
        sender = request.form.get("sender", "").strip()
        receiver = request.form.get("receiver", "").strip()
        custom_messages = request.form.get("custom_messages", "").strip()
        song_file = request.files.get('song_file')
        audio_path = None
        if song_file and song_file.filename:
            filename = secure_filename(song_file.filename)
            temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[1])
            song_file.save(temp_audio.name)
            audio_path = temp_audio.name

        # Validate names
        sender_valid, sender_errors = validate_name(sender, "sender")
        receiver_valid, receiver_errors = validate_name(receiver, "receiver")

        if sender_errors or receiver_errors:
            flash("Erreur de validation : " + "; ".join(sender_errors + receiver_errors), "error")
            if audio_path:
                os.unlink(audio_path)
            return render_template("index.html", messages=messages, lover_name=lover_name, sender_name=sender_name, video_url=video_url)

        lover_name = receiver_valid
        sender_name = sender_valid

        # Get messages
        if custom_messages:
            raw_msgs = [msg.strip() for msg in custom_messages.split('\n') if msg.strip()]
            messages = [{'text': msg} for msg in raw_msgs]
        else:
            try:
                raw_messages = load_messages()
                if raw_messages:
                    raw_msgs = personalize_messages(raw_messages, lover_name, sender_name)
                    messages = [{'text': msg['text']} for msg in raw_msgs]
                else:
                    flash("Error: Unable to load messages.", "error")
                    messages = []
            except Exception as e:
                flash("Error processing messages.", "error")
                messages = []

        # Generate video if messages exist
        if messages:
            try:
                video_path = generate_video(messages, audio_path)
                video_url = url_for('home.download_video', filename=os.path.basename(video_path))
            except Exception as e:
                flash(f"Erreur lors de la génération de la vidéo : {str(e)}", "error")
            finally:
                if audio_path:
                    os.unlink(audio_path)

    else:
        # GET: default
        try:
            raw_messages = load_messages()
            if raw_messages:
                raw_msgs = personalize_messages(raw_messages, lover_name, sender_name)
                messages = [{'text': msg['text']} for msg in raw_msgs]
            else:
                flash("Error: Unable to load messages.", "error")
        except Exception as e:
            flash("Error processing messages.", "error")
            messages = []

    # Prepare custom messages text for textarea
    custom_messages_text = '\n'.join(msg['text'] for msg in messages) if messages else ''
    show_form = request.method == 'GET' or not messages  # Show form on GET or if no messages

    # Render template
    return render_template(
        "index.html",
        messages=messages,
        lover_name=lover_name,
        sender_name=sender_name,
        video_url=video_url,
        custom_messages_text=custom_messages_text,
        show_form=show_form
    )


def generate_video(messages, audio_path):
    """
    Generate a video with text clips for messages and optional audio.

    Args:
        messages (list): List of message texts.
        audio_path (str): Path to audio file, or None.

    Returns:
        str: Path to the generated video file.
    """
    clips = []
    duration_per_message = 3  # seconds per message

    for msg in messages:
        # Create text clip
        txt_clip = TextClip(msg['text']).set_font('DejaVuSans-Bold').set_color('white').set_size((1280, 720)).set_duration(duration_per_message)
        clips.append(txt_clip)

    # Concatenate clips
    video = concatenate_videoclips(clips, method="compose")

    # Add audio if provided
    if audio_path:
        try:
            audio = AudioFileClip(audio_path).set_duration(video.duration)
            video = video.set_audio(audio)
        except Exception as e:
            # If audio fails, continue without
            pass

    # Export video
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    video.write_videofile(temp_video.name, fps=24, codec='libx264', audio_codec='aac')
    return temp_video.name


@home_bp.route("/download/<filename>")
def download_video(filename):
    """
    Serve the generated video file for download.

    Args:
        filename (str): Name of the video file.

    Returns:
        Response: File download response.
    """
    # For security, store videos in a temp dir and serve from there
    # Assuming videos are in temp dir
    path = os.path.join(tempfile.gettempdir(), filename)
    return send_file(path, as_attachment=True, download_name='love_video.mp4')
