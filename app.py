import streamlit as st
import os
import time
import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from datetime import datetime
from PIL import Image
from io import BytesIO
from reportlab.lib.utils import ImageReader


slides_folder = "slides"

questions = [
    {
        "question": "What is the primary mode of hepatitis B transmission?",
        "options": ["A. Sexual contact", "B. Sharing needles", "C. Mother to child during childbirth", "D. All of the above"],
        "correct_answer": "D. All of the above",
    },
    {
        "question": "How is hepatitis B primarily transmitted?",
        "options": ["A. Contaminated food and water", "B. Airborne droplets", "C. Sexual contact with an infected person", "D. Mosquito bites"],
        "correct_answer": "C. Sexual contact with an infected person",
    },
    {
        "question": "What is the incubation period of hepatitis B?",
        "options": ["A. 1 week", "B. 1 month", "C. 3 months", "D. 6 months"],
        "correct_answer": "C. 3 months",
    },
    {
        "question": "Which of the following is a symptom of acute hepatitis B infection?",
        "options": ["A. Jaundice", "B. Abdominal pain", "C. Fatigue", "D. All of the above"],
        "correct_answer": "D. All of the above",
    },
    {
        "question": "What percentage of adults clear the hepatitis B virus without treatment?",
        "options": ["A. 10%", "B. 25%", "C. 50%", "D. 90%"],
        "correct_answer": "D. 90%",
    },
    {
        "question": "Which hepatitis B antigen is the earliest marker of infection?",
        "options": ["A. HBsAg", "B. HBeAg", "C. Anti-HBc IgM", "D. Anti-HBs"],
        "correct_answer": "A. HBsAg",
    },
    {
        "question": "What is the recommended vaccine schedule for hepatitis B?",
        "options": ["A. One dose", "B. Two doses", "C. Three doses", "D. Four doses"],
        "correct_answer": "C. Three doses",
    },
    {
        "question": "Which of the following is a risk factor for hepatitis B infection?",
        "options": ["A. Smoking", "B. Obesity", "C. Injection drug use", "D. Vegetarian diet"],
        "correct_answer": "C. Injection drug use",
    },
    {
        "question": "What are the criteria for starting treatment for chronic hepatitis B?",
        "options": ["A. Elevated liver enzymes", "B. High viral load", "C. Liver fibrosis or cirrhosis", "D. All of the above"],
        "correct_answer": "D. All of the above",
    },
    {
        "question": "Which of the following is a complication of chronic hepatitis B?",
        "options": ["A. Liver failure", "B. Kidney stones", "C. Asthma", "D. Migraine"],
        "correct_answer": "A. Liver failure",
    },
    
]





def get_user_selections():
    if "selected_topic" not in st.session_state:
        st.session_state.selected_topic = "Introduction"
    return st.session_state.selected_topic        



def topic_1():
    st.title("Introduction to Hepatitis B")
    
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        # Embed YouTube video
        st.subheader("Watch Introduction Video")
        video_url = "https://www.youtube.com/embed/Uos0zzzQ_Bw"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        
        st.write("---")
        st.subheader("Question 1: What is the primary mode of hepatitis B transmission?")
        options_1 = ["A. Sexual contact", "B. Sharing needles", "C. Mother to child during childbirth", "D. All of the above"]
        correct_answer_1 = "D. All of the above"

        user_choice_1 = st.radio("Select your answer:", ["None"] + options_1)

        if user_choice_1 != "None":
            if user_choice_1 == correct_answer_1:
                st.success("Correct! All of the above are primary modes of hepatitis B transmission.")
            else:
                st.error(f"Wrong! The correct answer is: {correct_answer_1}")

        # Quiz 2: How is hepatitis B primarily transmitted?
        st.write("---")
        st.subheader("Question 2: How is hepatitis B primarily transmitted?")
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


                
    with rt_col:
        slides_folder = "slides/slide1"  
        st.subheader("Study accompanying info alongside the video")
        infographic_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide6.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide7.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide8.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide9.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide10.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide11.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        infographic_image = os.path.join(slides_folder, "Slide12.jpeg")
        st.image(infographic_image,use_column_width=True, caption="Introduction")
        

    


def topic_2():
    st.title("Modes of Transmission of HBV")
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        st.subheader("Watch Modes of Transmission of Hepatitis B Video")
        video_url = "https://www.youtube.com/embed/xg5yRly4cHA"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("---")
    with rt_col:  
        slides_folder = "slides/slide2" 
        st.subheader("Study accompanying info alongside the video")
        transmission_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
        transmission_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
        transmission_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
        transmission_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
        transmission_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
        transmission_image = os.path.join(slides_folder, "Slide6.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
        transmission_image = os.path.join(slides_folder, "Slide7.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
        transmission_image = os.path.join(slides_folder, "Slide8.jpeg")
        st.image(transmission_image,use_column_width=True, caption="Transmission of HBV")
    
    
    
def topic_3():
    st.title("Prevention of HBV")
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        st.subheader("Watch the Modes of Prevention of Hepatitis B Video")
        video_url = "https://www.youtube.com/embed/3S9k_UELJzs"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("---")
    with rt_col:
        slides_folder = "slides/slide3" 
        st.subheader("Study accompanying info alongside the video")
        prevention_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide6.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide7.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide8.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide9.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide10.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
        prevention_image = os.path.join(slides_folder, "Slide11.jpeg")
        st.image(prevention_image,use_column_width=True, caption="Prevention of HBV")
    
    
    
    
    
def topic_4():
    st.title("Prevention of Mother to Child Transmission of HBV")
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        st.subheader("Watch Prevention of Mother to Child transmission of Hepatitis B Video")
        video_url = "https://www.youtube.com/embed/UC_j9EWTy9Q"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("---")
    with rt_col:
        slides_folder = "slides/slide4"   
        st.subheader("Study accompanying info alongside the video")
        pmtct_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(pmtct_image,use_column_width=True, caption="PMTCT of HBV")
        pmtct_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(pmtct_image,use_column_width=True, caption="Prevention of sexual transmission")
        pmtct_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(pmtct_image,use_column_width=True, caption="Prevention in healthcare workers")
        pmtct_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(pmtct_image,use_column_width=True, caption="Other exposures of HBV")
        pmtct_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(pmtct_image,use_column_width=True, caption="Transplant recipients")
    
    
    
def topic_5():
    st.title("Symptoms, Signs & Outcomes of HBV Infection")
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        st.subheader("Watch the Symptoms and Signs of Hepatitis B Video")
        video_url = "https://www.youtube.com/embed/kiksNqIxcz8"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("---")
    with rt_col:
        slides_folder = "slides/slide5" 
        st.subheader("Study accompanying info alongside the video")
        ss_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
        ss_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
        ss_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
        ss_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
        ss_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
        ss_image = os.path.join(slides_folder, "Slide6.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
        ss_image = os.path.join(slides_folder, "Slide7.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
        ss_image = os.path.join(slides_folder, "Slide8.jpeg")
        st.image(ss_image,use_column_width=True, caption="Symptoms & Signs of HBV")
    
    
def topic_6():
    st.title("Understanding Laboratory Tests for HBV")
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        st.subheader("Watch Understanding Hepatitis B Serology Video")
        video_url = "https://www.youtube.com/embed/zlZ18zwG_70"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("---")
    with rt_col:  
        slides_folder = "slides/slide6" 
        st.subheader("Study accompanying info alongside the video")
        lab_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(lab_image,use_column_width=True, caption="Understanding lab results of HBV")
        lab_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(lab_image,use_column_width=True, caption="Understanding lab results of HBV")
        lab_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(lab_image,use_column_width=True, caption="Understanding lab results of HBV")
        lab_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(lab_image,use_column_width=True, caption="Understanding lab results of HBV")
        lab_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(lab_image,use_column_width=True, caption="Understanding lab results of HBV")
    
    
    
def topic_7():
    st.title("Outcome & Treatment of Acute HBV Infection")
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        st.subheader("Watch Outcome & Treatment of Acute HBV Video")
        video_url = "https://www.youtube.com/embed/V-y-SEq2-hM"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("---")
    with rt_col:  
        slides_folder = "slides/slide7" 
        st.subheader("Study accompanying info alongside the video")
        ot_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(ot_image,use_column_width=True, caption="Outcome & Treatment of HBV")
        ot_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(ot_image,use_column_width=True, caption="Outcome & Treatment of HBV")
        ot_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(ot_image,use_column_width=True, caption="Outcome & Treatment of HBV")
        ot_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(ot_image,use_column_width=True, caption="Outcome & Treatment of HBV")
        ot_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(ot_image,use_column_width=True, caption="Outcome & Treatment of HBV")
    
    

def topic_8():
    st.title("Criteria for Treatment of Chronic HBV Infection")
    lt_col,rt_col= st.columns([3,2])
    with lt_col:
        st.subheader("Watch Outcome & Treatment of Acute HBV Video")
        video_url = "https://www.youtube.com/embed/JX36tGZY1ME"
        st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.write("---")
    with rt_col:  
        slides_folder = "slides/slide8" 
        st.subheader("Study accompanying info alongside the video")
        criteria_image = os.path.join(slides_folder, "Slide1.jpeg")
        st.image(criteria_image,use_column_width=True, caption="Treatment criteria for chronic HBV")
        criteria_image = os.path.join(slides_folder, "Slide2.jpeg")
        st.image(criteria_image,use_column_width=True, caption="Treatment criteria for chronic HBV")
        criteria_image = os.path.join(slides_folder, "Slide3.jpeg")
        st.image(criteria_image,use_column_width=True, caption="Treatment criteria for chronic HBV")
        criteria_image = os.path.join(slides_folder, "Slide4.jpeg")
        st.image(criteria_image,use_column_width=True, caption="Treatment criteria for chronic HBV")
        criteria_image = os.path.join(slides_folder, "Slide5.jpeg")
        st.image(criteria_image,use_column_width=True, caption="Treatment criteria for chronic HBV")
    
def topic_9():
    global user_score
    st.title("Post Course Assessment")  
    st.write("Only attempt this assessment after you have gone through the course materials. Or you may wish to use it to guage the need to go through the learning materials.")
    # Number of correct answers
    num_correct = 0
    
    # Display the quiz questions and get user answers
    for i, question in enumerate(questions):
        st.write(f"---\nQuestion {i+1}: {question['question']}")
        user_choice = st.radio("Select your answer:", ["None"] + question["options"], key=i)
        
        if user_choice == question["correct_answer"]:
            num_correct += 1
    
    
    if num_correct > 0:
        user_score = (num_correct / len(questions)) * 100
        if user_score >= 80:
            # Display an input field for the user to enter their name within a form
            with st.form("certificate_form"):
                user_name = st.text_input("Enter your name:")
                generate_cert_button = st.form_submit_button("Generate Certificate")
            
            if generate_cert_button and user_name.strip() != "":
                certificate_file = generate_certificate(user_name, user_score)
                # Provide a link or button to download the certificate
                st.success("Certificate generated successfully!")
                download_file(certificate_file)
                
            elif generate_cert_button and user_name.strip() == "":
                st.warning("Please enter your name to generate the certificate.")
        else:
            st.error(f"Your score is {user_score:.2f}%.\nPlease review the materials and try the quiz again.")
            
def download_file(path):
    with open(path, "rb") as file:
        btn = st.download_button("Download Certificate", file.read(), file.name)
        
def generate_certificate(user_name, user_score):
    certificate_folder = "slides"
    certificate_file = os.path.join(certificate_folder, "certificate.pdf")

    completion_date = datetime.now().strftime("%B %d, %Y")

    # Set the page size to landscape mode
    c = canvas.Canvas(certificate_file, pagesize=landscape(letter))

    # Set the font size and style
    c.setFont("Helvetica-Bold", 20)

    # Calculate the width and height of the page
    height, width = landscape(letter)

   
    cert_bg_path = os.path.join(os.getcwd(), "slides", "border.png")
    # Use cert_bg_path as the design_frame_path
    design_frame_path = cert_bg_path
    # Draw the design frame on the certificate
    c.drawImage(design_frame_path, 0, 0, width=height, height=width, preserveAspectRatio=True)

    # Add the title at the top
    title = "Certificate of Achievement"
    title_width = c.stringWidth(title, "Helvetica-Bold", 40)
    title_x = (height - title_width) / 2  # Swap width and height for landscape
    title_y = width - 120  # Swap width and height for landscape
    c.setFillColor("black")  # Set the text color to white
    c.setFont("Helvetica-Bold", 40)
    c.drawString(title_x, title_y, title)

    # Set the font size and color for the rest of the content
    c.setFont("Helvetica", 20)
    c.setFillColor("black")  # Set the text color to white

    user_name_font = "Helvetica-BoldOblique"
    user_name_font_size = 24
    
    

    # Separate the text into three rows
    row1 = "This is to certify that"
    row2 = user_name  # Use the user's name directly
    row3 = "has successfully completed the Hepatitis B Course."

    # Calculate the width of each row
    row1_width = c.stringWidth(row1, "Helvetica", 14)
    row2_width = c.stringWidth(row2, user_name_font, user_name_font_size)  # Use the new font and font size
    row3_width = c.stringWidth(row3, "Helvetica", 14)

    # Calculate the starting X position for each row to center them
    row1_x = (height - row1_width) / 2  # Swap width and height for landscape
    row2_x = (height - row2_width) / 2  # Swap width and height for landscape
    row3_x = (height - row3_width) / 2  # Swap width and height for landscape

    # Calculate the Y position for each row to separate them vertically
    row1_y = title_y - 80  # Adjust this value to create space between the title and row1
    row2_y = row1_y - 40  # Adjust this value to create space between row1 and row2
    row3_y = row2_y - 40  # Adjust this value to create space between row2 and row3

    # Draw each row separately
    c.drawString(row1_x, row1_y, row1)
    c.setFont(user_name_font, user_name_font_size)  # Set the font and font size for the user's name
    c.drawString(row2_x, row2_y, row2)
    c.setFont("Helvetica", 14)  # Reset the font and font size to default for the rest of the content
    c.drawString(row3_x, row3_y, row3)

    # Add the completion date on the lower left
    date_x = 120
    date_y = 100
    c.drawString(date_x, date_y, f"Date: {completion_date}")

    # Add the score just above the date
    score_x = date_x + 150
    score_y = date_y + 100
    c.drawString(score_x, score_y, f"Score: {user_score:.1f}%")

   # Add the course coordinator on the lower right
    coordinator_text = "Director: Dr. N.G. Ladep"
    coordinator_text_width = c.stringWidth(coordinator_text, "Helvetica", 20)
    coordinator_x = width - coordinator_text_width - 50  # Increase the space between date and coordinator horizontally
    coordinator_y = date_y # Keep the vertical position the same
    c.drawString(coordinator_x, coordinator_y, coordinator_text)

    # Save the certificate
    c.save()

    return certificate_file


def main():
    st.title("🦠 Hepatitis B Course")
    slides_folder = "slides"  
    left_column, right_column=st.columns([1,1])
    with left_column:
        infographic_image = os.path.join(slides_folder, "intro.png")
        st.image(infographic_image,width=325, caption="Source: by NG Ladep")
    with right_column:
        st.subheader(" Author - Dr. Nimzing Ladep MBBS PhD FRCP, Consultant Hepatologist")
        st.write("Welcome to this Hepatitis B Course!")
        
    
    
    

    st.subheader("""
                 Use topic area below 'Select a Topic' to navigate contents.
                 - Each of the 8 topic areas have illustrated contents and a video 
                 - The video could be played whilst the user can study the infographics
                 - Should you prefer to watch only, then you can go straight to the video
                 - Attempt the quizzes as you go through the 8 topics
                 - From transmission to treatment of Hepatitis B infection
                 """
        
        )
    
    
    # List of bundled slide PDFs
    image_based_topics = {
        "Introduction": topic_1,
        "Modes of Transmission of HBV": topic_2,
        "Prevention of HBV": topic_3,
        "Prevention of Mother to Child Transmission of HBV": topic_4,
        "Symptoms, Signs & Outcomes of HBV Infection": topic_5,
        "Understanding Laboratory Tests for HBV": topic_6,
        "Outcome & Treatment of Acute HBV Infection": topic_7,
        "Criteria for Treatment of Chronic HBV Infection":topic_8,
        "Post Course Assessment":topic_9
    }

    # Get the selected topic from the user
    selected_topic = st.selectbox("Select a Topic", list(image_based_topics.keys()), index=list(image_based_topics.keys()).index(get_user_selections()))
    # Store the selected topic in session_state
    st.session_state.selected_topic = selected_topic
    
    if st.button("🔍 Load Topic"):
        progress_bar = st.empty()  # Create a placeholder for the progress bar
        with st.spinner("Loading..."):
            # Simulate some time-consuming operation (e.g., fetching data or processing)
            for i in range(100):
                time.sleep(0.01)  # Simulating some processing delay
                progress_bar.progress(i + 1)  # Update the progress bar value
            st.success("Topic loaded successfully!")
            
            
                
    st.markdown(f"<h2 style='text-align:center;color:#ff0000;'>{selected_topic}</h2>", unsafe_allow_html=True)

    # Call the corresponding topic function based on user selection
    image_based_topics[selected_topic]()
    
    


    

if __name__ == "__main__":
    main()
