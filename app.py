import streamlit as st
from pdf2image import convert_from_path
import os

slides_folder = "slides"

def display_pdf_slide(pdf_path):
    images = convert_from_path(pdf_path)

    for image in images:
        st.image(image, use_column_width=True)

        



def topic_1():
    st.title("Introduction to Hepatitis B")
    
    pdf_path = os.path.join(slides_folder, "slide1.pdf")
    display_pdf_slide(pdf_path)
    

    # Quiz 1: What is the primary mode of hepatitis B transmission?
    st.header("Quiz 1: What is the primary mode of hepatitis B transmission?")
    options_1 = ["A. Sexual contact", "B. Sharing needles", "C. Mother to child during childbirth", "D. All of the above"]
    correct_answer_1 = "D. All of the above"

    user_choice_1 = st.radio("Select your answer:", ["None"] + options_1)

    if user_choice_1 != "None":
        if user_choice_1 == correct_answer_1:
            st.success("Correct! All of the above are primary modes of hepatitis B transmission.")
        else:
            st.error(f"Wrong! The correct answer is: {correct_answer_1}")

    # Quiz 2: How is hepatitis B primarily transmitted?
    st.header("Quiz 2: How is hepatitis B primarily transmitted?")
    options_2 = ["A. Contaminated food and water", "B. Airborne droplets", "C. Sexual contact with an infected person", "D. Mosquito bites"]
    correct_answer_2 = "C. Sexual contact with an infected person"

    # Generate a unique key for the second radio button using the question text
    question_key_2 = hash("Select your answer for Quiz 2:")
    user_choice_2 = st.radio("Select your answer:", ["None"] + options_2, key=question_key_2)

    if user_choice_2 != "None":
        if user_choice_2 == correct_answer_2:
            st.success("Correct! Sexual contact with an infected person is the primary mode of hepatitis B transmission.")
        else:
            st.error(f"Wrong! The correct answer is: {correct_answer_2}")
            
    # Embed YouTube video
    st.header("Watch the Introduction Video")
    video_url = "https://www.youtube.com/embed/Uos0zzzQ_Bw"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)




def topic_2():
    st.title("Modes of Transmission of HBV")
    pdf_path = os.path.join(slides_folder, "slide2.pdf")
    display_pdf_slide(pdf_path)
    
    # Embed YouTube video
    st.header("Watch the Modes of Transmission of Hepatitis B Video")
    video_url = "https://www.youtube.com/embed/xg5yRly4cHA"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    
def topic_3():
    st.title("Prevention of HBV")
    pdf_path = os.path.join(slides_folder, "slide3.pdf")
    display_pdf_slide(pdf_path)
    
    # Embed YouTube video
    st.header("Watch the Modes of Prevention of Hepatitis B Video")
    video_url = "https://www.youtube.com/embed/3S9k_UELJzs"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    
def topic_4():
    st.title("Prevention of Mother to Child Transmission of HBV")
    pdf_path = os.path.join(slides_folder, "slide4.pdf")
    display_pdf_slide(pdf_path)
    # Embed YouTube video
    st.header("Watch the Modes of Prevention of Hepatitis B Video")
    video_url = "https://www.youtube.com/embed/UC_j9EWTy9Q"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    
def topic_5():
    st.title("Symptoms, Signs & Outcomes of HBV Infection")
    pdf_path = os.path.join(slides_folder, "slide5.pdf")
    display_pdf_slide(pdf_path)
    # Embed YouTube video
    st.header("Watch the Symptoms and Signs of Hepatitis B Video")
    video_url = "https://www.youtube.com/embed/kiksNqIxcz8"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    
def topic_6():
    st.title("Understanding Laboratory Tests for HBV")
    pdf_path = os.path.join(slides_folder, "slide6.pdf")
    display_pdf_slide(pdf_path)
    # Embed YouTube video
    st.header("Watch Understanding Hepatitis B Serology Video")
    video_url = "https://www.youtube.com/embed/zlZ18zwG_70"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    
def topic_7():
    st.title("Outcome & Treatment of Acute HBV Infection")
    pdf_path = os.path.join(slides_folder, "slide7.pdf")
    display_pdf_slide(pdf_path)
    # Embed YouTube video
    st.header("Watch Outcome & Treatment of Acute HBV Video")
    video_url = "https://www.youtube.com/embed/V-y-SEq2-hM"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

def topic_8():
    st.title("Criteria for Treatment of Chronic HBV Infection")
    pdf_path = os.path.join(slides_folder, "slide8.pdf")
    display_pdf_slide(pdf_path)
    # Embed YouTube video
    st.header("Watch Criteria for Treatment of Chronic HBV Video")
    video_url = "https://www.youtube.com/embed/JX36tGZY1ME"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    
    # Add any interactive elements, quizzes, or additional resources for Topic 2

# Define functions for the other topics (topic_3 to topic_8)

def main():
    st.title("🦠 Hepatitis B Course")
    slides_folder = "slides"  # Folder name where the slides are located
    infographic_image = os.path.join(slides_folder, "intro.png")
    st.image(infographic_image, use_column_width=True, caption="Source: by NG Ladep")
    st.subheader(" By - Dr. Nimzing Ladep MBBS PhD FRCP, Consultant Hepatologist")
    st.write("Welcome to this Hepatitis B Course!")
    
    

    st.subheader("""
                 Use topic area below 'Select a Topic' to navigate contents.
                 - Each of the 8 topic areas have illustrated contents and a video 
                 - The video is located at the end of each topic
                 - Should you prefer to watch, then you can go straight to the video
                 - If you wish to read the contents, they are self explanatory
                 - From transmission to treatment of Hepatitis B infection
                 """
        
        )
    # List of bundled slide PDFs
    bundled_slides = {
        "Introduction": "slides/slide1.pdf",
        "Modes of Transmission of HBV": "slides/slide2.pdf",
        "Prevention of HBV": "slides/slide3.pdf",
        "Prevention of Mother to Child Transmission of HBV": "slides/slide4.pdf",
        "Symptoms, Signs & Outcomes of HBV Infection": "slides/slide5.pdf",
        "Understanding Laboratory Tests for HBV": "slides/slide6.pdf",
        "Outcome & Treatment of Acute HBV Infection": "slides/slide7.pdf",
        "Criteria for Treatment of Chronic HBV Infection": "slides/slide8.pdf",
        # Add more bundled slides as needed
    }

    # Topic selection
    selected_topic = st.selectbox("Select a Topic", list(bundled_slides.keys()))

    # Apply custom CSS style to make the selected topic prominent
    st.markdown(f"<h2 style='text-align:center;color:#ff0000;'>{selected_topic}</h2>", unsafe_allow_html=True)


    # Call the corresponding topic function based on user selection
    if selected_topic == "Introduction":
        topic_1()
    elif selected_topic == "Modes of Transmission of HBV":
        topic_2()
    elif selected_topic == "Prevention of HBV":
        topic_3()
    elif selected_topic == "Prevention of Mother to Child Transmission of HBV":
        topic_4()
    elif selected_topic == "Symptoms, Signs & Outcomes of HBV Infection":
        topic_5()
    elif selected_topic == "Understanding Laboratory Tests for HBV":
        topic_6()
    elif selected_topic == "Outcome & Treatment of Acute HBV Infection":
        topic_7()
    elif selected_topic == "Criteria for Treatment of Chronic HBV Infection":
        topic_8()
    # Call functions for the other topics (topic_3 to topic_8) here

if __name__ == "__main__":
    main()
