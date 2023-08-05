import streamlit as st
import os
import time




slides_folder = "slides"




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
    
    # Embed YouTube video
    
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
                 - The video is located at the end of each topic
                 - Should you prefer to watch, then you can go straight to the video
                 - If you wish to read the contents, they are self explanatory
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
        # Add more bundled slides as needed
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
