import streamlit as st
import streamlit.components.v1 as components
import base64
import re  # Import the regular expression module

def image_to_base64(image_path):
    """Converts an image to a Base64 string."""
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            return f"data:image/jpeg;base64,{encoded_string}"  # Adjust if needed (png, gif, etc.)
    except FileNotFoundError:
        st.error(f"Error: Image file not found at {image_path}")
        return ""
    except Exception as e:
        st.error(f"An error occurred during image encoding: {e}")
        return ""

def render_html(html_file_path, cat_base64, profile_base64):
    """Renders HTML with Base64 images using regex."""
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_string = f.read()

            # Use regex to replace the src attribute *only*
            html_string = re.sub(r'src="cat\.jpg"', f'src="{cat_base64}"', html_string)
            html_string = re.sub(r'src="profile\.jpg"', f'src="{profile_base64}"', html_string)

            components.html(html_string, height=800, scrolling=True)
    except FileNotFoundError:
        st.error(f"Error: HTML file not found at {html_file_path}")
    except Exception as e:
        st.error(f"An error occurred during HTML rendering: {e}")


st.title("Mittens: The Velvet Pawed Tyrant")

cat_base64 = image_to_base64("cat.jpg")
profile_base64 = image_to_base64("profile.jpg")

if cat_base64 and profile_base64:
    render_html("mittens.html", cat_base64, profile_base64)
else:
    st.error("Could not load images. Please check the file paths.")