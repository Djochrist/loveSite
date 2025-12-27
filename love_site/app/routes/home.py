"""
Main routes for the love_site application.

This module defines Flask endpoints for the user interface,
handling form display and rendering of personalized messages.
"""

import os
import re
import tempfile
import logging
from pathlib import Path
from flask import Blueprint, render_template, request, flash, send_file, url_for, current_app, abort
from moviepy import TextClip, concatenate_videoclips, AudioFileClip, ColorClip, CompositeVideoClip
from moviepy.editor import ImageSequenceClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import textwrap
import random
import threading
from werkzeug.utils import secure_filename

from ..services.messages import load_messages, personalize_messages

# Blueprint for home page routes
home_bp = Blueprint("home", __name__)

# Set up logging
logger = logging.getLogger(__name__)


def allowed_file(filename):
    """
    Check if uploaded file has an allowed extension.

    Args:
        filename (str): The filename to check.

    Returns:
        bool: True if allowed, False otherwise.
    """
    if not filename:
        return False
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


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

        # Validate request size early
        try:
            content_length = request.content_length
        except Exception:
            content_length = None
        if content_length and current_app.config.get('MAX_CONTENT_LENGTH') and content_length > current_app.config['MAX_CONTENT_LENGTH']:
            flash("Le fichier est trop volumineux (maximum 50MB).", "error")
            return render_template("index.html", messages=messages, lover_name=lover_name, sender_name=sender_name, video_url=video_url)

        # Validate file upload
        if song_file and song_file.filename:
            if not allowed_file(song_file.filename):
                flash("Type de fichier audio non autorisé. Utilisez MP3, WAV, M4A, AAC, OGG, WebM, MP4 ou AVI.", "error")
                return render_template("index.html", messages=messages, lover_name=lover_name, sender_name=sender_name, video_url=video_url)

            filename = secure_filename(song_file.filename)
            # Check file size (50MB limit)
            song_file.seek(0, os.SEEK_END)
            file_size = song_file.tell()
            song_file.seek(0)
            if file_size > current_app.config['MAX_CONTENT_LENGTH']:
                flash("Le fichier audio est trop volumineux (maximum 50MB).", "error")
                return render_template("index.html", messages=messages, lover_name=lover_name, sender_name=sender_name, video_url=video_url)

            temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[1])
            song_file.save(temp_audio.name)
            audio_path = temp_audio.name

        # Validate names
        sender_valid, sender_errors = validate_name(sender, "sender")
        receiver_valid, receiver_errors = validate_name(receiver, "receiver")

        if sender_errors or receiver_errors:
            flash("Erreur de validation : " + "; ".join(sender_errors + receiver_errors), "error")
            if audio_path and os.path.exists(audio_path):
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
                logger.exception('Video generation failed')
                flash(f"Erreur lors de la génération de la vidéo : {str(e)}", "error")
            finally:
                if audio_path:
                    try:
                        os.unlink(audio_path)
                    except Exception:
                        logger.exception('Failed to remove temp audio')

    else:
        # GET: default
            try:
                raw_messages = load_messages()
                if raw_messages:
                    raw_msgs = personalize_messages(raw_messages, lover_name, sender_name)
                    messages = [{'text': msg['text']} for msg in raw_msgs]
                else:
                    flash("Error: Unable to load messages.", "error")
            except Exception:
                logger.exception('Error processing messages')
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

    else:
        # GET: default
        try:
            raw_messages = load_messages()
            if raw_messages:
                raw_msgs = personalize_messages(raw_messages, lover_name, sender_name)
                messages = [{'text': msg['text']} for msg in raw_msgs]
            else:
                flash("Error: Unable to load messages.", "error")
        except Exception:
            logger.exception('Error processing messages (GET)')
            flash("Error processing messages.", "error")
            messages = []
    possible_fonts = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        'DejaVuSans-Bold',
        'DejaVuSans'
    ]

    for msg in messages:
        # Create text clip with better styling
        txt_clip = TextClip(
            text=msg['text'],
            color='white',
            size=(1920, 1080),
            # Parameters
            fps = current_app.config.get('VIDEO_FPS', 24)
            width = current_app.config.get('VIDEO_WIDTH', 1920)
            height = current_app.config.get('VIDEO_HEIGHT', 1080)
            duration_per_message = 4  # seconds per message
            frames_per_message = int(fps * duration_per_message)

            # Find available font
            possible_fonts = [
                '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
                '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
                '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
            ]
            font_path = None
            for p in possible_fonts:
                try:
                    ImageFont.truetype(p, 24)
                    font_path = p
                    break
                except Exception:
                    continue

            def _draw_heart(draw, x, y, size, color=(255, 50, 80, 255)):
                # Draw a simple heart using two circles and a triangle
                r = size // 4
                # left circle
                draw.ellipse((x - r - r//2, y - r, x - r//2, y + r), fill=color)
                # right circle
                draw.ellipse((x + r//2, y - r, x + r + r//2, y + r), fill=color)
                # bottom triangle
                draw.polygon([(x - r - r//2 + r//2, y + r), (x + r + r//2 - r//2, y + r), (x, y + size)], fill=color)

            clips = []
            for midx, msg in enumerate(messages):
                text = msg.get('text', '')
                # Wrap text to fit width
                wrap_width = 40
                wrapped = textwrap.fill(text, width=wrap_width)

                # Deterministic random for each message so animation is reproducible
                rnd = random.Random(midx)

                frames = []
                for f in range(frames_per_message):
                    t = f / fps
                    # Create background
                    img = Image.new('RGBA', (width, height), (20, 20, 50, 255))
                    draw = ImageDraw.Draw(img, 'RGBA')

                    # Draw message text centered
                    try:
                        if font_path:
                            font = ImageFont.truetype(font_path, size=64)
                        else:
                            font = ImageFont.load_default()
                    except Exception:
                        font = ImageFont.load_default()

                    # compute text size and position
                    lines = wrapped.split('\n')
                    total_h = 0
                    line_sizes = []
                    for line in lines:
                        wtxt, htxt = draw.textsize(line, font=font)
                        line_sizes.append((wtxt, htxt))
                        total_h += htxt + 10

                    y_text = (height - total_h) // 2
                    for i, line in enumerate(lines):
                        wtxt, htxt = line_sizes[i]
                        x_text = (width - wtxt) // 2
                        draw.text((x_text, y_text), line, font=font, fill=(255, 255, 255, 255))
                        y_text += htxt + 10

                    # Draw animated hearts
                    heart_count = 8
                    for hi in range(heart_count):
                        # Each heart has a seed depending on hi and midx
                        seed = rnd.randint(0, 100000) + hi
                        rng = random.Random(seed)
                        # Initial position around bottom center
                        base_x = width // 2 + rng.randint(-200, 200)
                        base_y = int(height * 0.75) + rng.randint(-50, 50)
                        # movement upward over time
                        progress = (f / frames_per_message)
                        dx = int((rng.random() - 0.5) * 400 * progress)
                        dy = int(-500 * progress + rng.randint(-30, 30) * progress)
                        size = int(30 + 60 * (0.5 + 0.5 * rng.random()) * (0.5 + progress))
                        alpha = int(255 * (1.0 - progress))
                        heart_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                        hdraw = ImageDraw.Draw(heart_img, 'RGBA')
                        _draw_heart(hdraw, base_x + dx, base_y + dy, size, color=(255, 60, 90, alpha))
                        img = Image.alpha_composite(img, heart_img)

                    frames.append(np.array(img.convert('RGB')))

                clip = ImageSequenceClip(frames, fps=fps)
                clip = clip.set_duration(duration_per_message)
                clips.append(clip)

            # Concatenate clips
            video = concatenate_videoclips(clips, method='compose')

            # Add audio if provided
            if audio_path:
                try:
                    audio = AudioFileClip(audio_path).with_duration(video.duration)
                    video = video.with_audio(audio)
                except Exception as e:
                    logger.warning(f"Failed to add audio to video: {e}")

            # Export video
            import tempfile as _tmp
            temp_video = _tmp.NamedTemporaryFile(delete=False, suffix='.mp4', dir=_tmp.gettempdir())
            video.write_videofile(temp_video.name, fps=fps, codec=current_app.config.get('VIDEO_CODEC', 'libx264'), audio_codec=current_app.config.get('AUDIO_CODEC', 'aac'))
            return temp_video.name

    # Ensure it ends with .mp4
    if not filename.endswith('.mp4'):
        logger.warning(f"Invalid file extension requested: {filename}")
        abort(400, "Invalid file type")

    # Build safe path in temp directory
    safe_path = os.path.join(tempfile.gettempdir(), filename)

    # Verify file exists and is in temp directory
    if not os.path.isfile(safe_path):
        logger.warning(f"Requested file does not exist: {safe_path}")
        abort(404, "File not found")

    # Additional security: Check if path is actually within temp directory
    temp_dir = tempfile.gettempdir()
    if not os.path.commonpath([safe_path, temp_dir]) == temp_dir:
        logger.warning(f"Path traversal attempt: {safe_path}")
        abort(400, "Invalid path")

    # Serve file and schedule deletion shortly after
    try:
        response = send_file(safe_path, as_attachment=True, download_name='love_video.mp4')
    except Exception:
        logger.exception(f'Failed to send file: {safe_path}')
        abort(500, "Failed to serve file")

    def _del_after(path, delay=60):
        try:
            time.sleep(delay)
            if os.path.exists(path):
                os.unlink(path)
                logger.info(f"Deleted temp video after download: {path}")
        except Exception:
            logger.exception(f"Failed to delete temp video: {path}")

    try:
        t = threading.Thread(target=_del_after, args=(safe_path, 60), daemon=True)
        t.start()
    except Exception:
        logger.exception('Failed to start deletion thread for downloaded file')

    return response
