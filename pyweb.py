import streamlit as st

st.title("Animalia Questionnaire")
st.write("Answer all questions below to identify the most likely animal.")

#Questions
q1 = st.selectbox("1. Where does the animal primarily live?", ["land", "water", "air"])
q2 = st.radio("2. Is it a domestic animal?", ["yes", "no"])
q3 = st.radio("3. Is the animal large (bigger than a human)?", ["yes", "no"])
q4 = st.radio("4. Does it have fur?", ["yes", "no"])
q5 = st.radio("5. Does it have legs?", ["yes", "no"])

if q5 == "yes":
    q6 = st.selectbox("6. How many legs?", ["0", "2", "4", "6", "8"])
else:
    q6 = "0"

q7 = st.selectbox("7. What does it eat?", ["herbivore", "carnivore", "omnivore"])
q8 = st.radio("8. Is it known for high speed?", ["yes", "no"])
q9 = st.radio("9. Does it make loud or noticeable sounds?", ["yes", "no"])
q10 = st.radio("10. Does it live in groups/packs/herds?", ["yes", "no"])

#Identification Logic
def identify_animal():
    # AIR ANIMALS
    if q1 == "air":
        if q7 == "carnivore":
            if q10 == "yes":
                return "Vulture (group scavenger)"
            else:
                return "Falcon or Eagle (solitary hunter)"
        else:
            if q9 == "yes":
                if q10 == "yes":
                    return "Parrot (social and noisy)"
                else:
                    return "Crow (noisy but not flock dependent)"
            else:
                if q10 == "yes":
                    return "Pigeon (flock-based)"
                else:
                    return "Sparrow"

    # WATER ANIMALS
    elif q1 == "water":
        if q7 == "carnivore":
            if q3 == "yes":
                if q10 == "yes":
                    return "Orca (killer whale pod)"
                else:
                    return "Shark (solitary predator)"
            else:
                if q10 == "yes":
                    return "Seal (social animal)"
                else:
                    return "Octopus (solitary)"
        else:
            if q10 == "yes":
                return "Dolphin (pod-based)"
            else:
                return "Whale or Manatee"

    # LAND ANIMALS
    elif q1 == "land":
        # Domestic
        if q2 == "yes":
            if q6 == "4":
                if q7 == "omnivore":
                    if q10 == "yes":
                        return "Dog (pack animal)"
                    else:
                        return "Cat (solitary nature)"
                elif q7 == "herbivore":
                    if q10 == "yes":
                        return "Cow or Sheep (herd animals)"
                    else:
                        return "Goat (less herd dependent)"
                else:
                    return "No common 4-legged domestic carnivores"
            elif q6 == "2":
                if q10 == "yes":
                    return "Chicken (flock bird)"
                else:
                    return "Duck or Rooster"
            else:
                if q10 == "yes":
                    return "Guinea Pig or Rabbit"
                else:
                    return "Pet Snake or Tortoise"

        # Wild
        else:
            if q3 == "yes":  # Large wild animals
                if q7 == "herbivore":
                    if q10 == "yes":
                        return "Elephant (large herds)"
                    else:
                        return "Rhinoceros (solitary)"
                elif q7 == "carnivore":
                    if q10 == "yes":
                        return "Lion (pride-living)"
                    else:
                        return "Tiger (solitary hunter)"
                else:
                    if q10 == "yes":
                        return "Brown Bear (group feeding)"
                    else:
                        return "Panda (solitary)"

            # Medium/Small wild animals
            else:
                if q6 == "4":
                    if q7 == "omnivore":
                        if q10 == "yes":
                            return "Monkey or Baboon"
                        else:
                            return "Raccoon or Small Bear"
                    elif q7 == "carnivore":
                        if q10 == "yes":
                            return "Wolf (pack animal)"
                        else:
                            return "Fox (solitary)"
                    else:
                        if q10 == "yes":
                            return "Deer (herd based)"
                        else:
                            return "Hippo (solitary tendency)"

                elif q6 == "2":
                    if q10 == "yes":
                        return "Ostrich (small herds)"
                    else:
                        return "Emu or Cassowary"

                elif q6 == "0":
                    if q7 == "carnivore":
                        if q10 == "yes":
                            return "Garter Snake (social species)"
                        else:
                            return "Cobra or Python"
                    else:
                        if q10 == "yes":
                            return "Earthworms (cluster behavior)"
                        else:
                            return "Lizard or Gecko"

                else:
                    if q10 == "yes":
                        return "Ant or Termite (colony based)"
                    else:
                        return "Spider (solitary)"

    return "Unable to classify the animal."


#Output
if st.button("Identify Animal"):
    result = identify_animal()
    st.subheader("Predicted Animal:")
    st.success(result)
