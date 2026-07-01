import streamlit as st
from ai_model import predict_ngo_category

# In-memory data storage (reset on every app reload)
if 'needy_people' not in st.session_state:
    st.session_state.needy_people = []

if 'ngos' not in st.session_state:
    st.session_state.ngos = []

if 'connections' not in st.session_state:
    st.session_state.connections = []

def register_needy():
    st.header("Register Needy Individual")
    with st.form("needy_form"):
        name = st.text_input("Name", "")
        age = st.number_input("Age", min_value=1, max_value=120, value=18)
        needs = st.text_area("Needs (comma separated)", "")
        location = st.text_input("Location (city)", "")
        skills = st.text_input("Skills (optional)", "")
        education_level = st.selectbox("Education Level", ["none", "middle school", "highschool", "college"])
        submitted = st.form_submit_button("Register Needy Individual")

        if submitted:
            new_person = {
                'id': len(st.session_state.needy_people) + 1,
                'name': name,
                'age': age,
                'needs': needs.lower(),
                'location': location.lower(),
                'skills': skills.lower(),
                'education_level': education_level.lower()
            }
            st.session_state.needy_people.append(new_person)

            # AI prediction of NGO category
            predicted_category = predict_ngo_category(age, education_level, needs.lower(), skills.lower()).lower()

            # Match NGOs by location and service
            matched_ngos = [ngo for ngo in st.session_state.ngos if (ngo['location'] == location.lower() and predicted_category in ngo['services'])]

            for ngo in matched_ngos:
                st.session_state.connections.append({'needy_id': new_person['id'], 'ngo_id': ngo['id']})

            st.success(f"Registered {name} and matched with {len(matched_ngos)} NGOs.")

def register_ngo():
    st.header("Register NGO / Community Group")
    with st.form("ngo_form"):
        name = st.text_input("NGO Name", "")
        location = st.text_input("Location (city)", "")
        services = st.text_area("Services offered (comma separated)", "")
        submitted = st.form_submit_button("Register NGO")

        if submitted:
            new_ngo = {
                'id': len(st.session_state.ngos) + 1,
                'name': name,
                'location': location.lower(),
                'services': services.lower()
            }
            st.session_state.ngos.append(new_ngo)
            st.success(f"Registered NGO {name}.")

def show_matches():
    st.header("Matched Needy Individuals with NGOs")
    if st.session_state.connections:
        for conn in st.session_state.connections:
            needy = next((n for n in st.session_state.needy_people if n['id'] == conn['needy_id']), None)
            ngo = next((g for g in st.session_state.ngos if g['id'] == conn['ngo_id']), None)
            if needy and ngo:
                st.markdown(f"**Needy Individual:** {needy['name']} (Needs: {needy['needs']}, Location: {needy['location']})")
                st.markdown(f"**Matched NGO:** {ngo['name']} (Services: {ngo['services']}, Location: {ngo['location']})")
                if st.button(f"View Recommendations for {needy['name']}", key=f"rec_{needy['id']}"):
                    show_recommendations(needy)
                st.markdown("---")
    else:
        st.info("No matches found yet.")

def show_recommendations(needy):
    st.subheader(f"Recommendations for {needy['name']}")
    recs = []
    age = needy['age']
    if age <= 18:
        recs.append("Enroll in local schools or free education programs.")
        recs.append("Access child welfare and nutrition programs.")
    elif 18 < age < 60:
        recs.append("Look for skill development courses.")
        recs.append("Employment assistance programs.")
        if needy['skills']:
            recs.append(f"Consider jobs related to your skills: {needy['skills']}")
    else:
        recs.append("Access elderly care services.")
        recs.append("Social welfare and health assistance.")
    for r in recs:
        st.write("- " + r)

def main():
    st.title("NeedyConnect - AI-powered NGO Matchmaking")

    menu = ["Home", "Register Needy Individual", "Register NGO", "View Matches"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Welcome to NeedyConnect! Use the sidebar to navigate.")
    elif choice == "Register Needy Individual":
        register_needy()
    elif choice == "Register NGO":
        register_ngo()
    elif choice == "View Matches":
        show_matches()

if __name__ == "__main__":
    main()