import re
import streamlit as st
import streamlit.components.v1 as components

st.write("# BNCC Classifier")

message_text = st.text_input("Enter a message for spam evaluation")

def preprocessor(text):
    # text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    # emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    # text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    print("Preprocessing...")
    return text

# model = joblib.load('spam_classifier.joblib')

# def classify_message(model, message):

	# label = model.predict([message])[0]
	# spam_prob = model.predict_proba([message])

	# return {'label': label, 'spam_probability': spam_prob[0][1]}

if message_text != '':

	# st.write(result)
	print("We have a text input...")
	explain_pred = st.button('Predict!')

	# if explain_pred:
		# with st.spinner('Classifying...'):
			# class_names = ['ham', 'spam']
			# components.html(exp.as_html(), height=800)

