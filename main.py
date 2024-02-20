import paddle
from paddle import inference
from transformers import BertTokenizer, BertForSequenceClassification
import torch


def speech_to_text(audio_file):
    # Initialize PaddleSpeech model
    config = inference.Config(
        "C:/Users/hp/OneDrive/Bureau/DeepSpeech/PaddleSpeech")  # Replace with the path to your PaddleSpeech model directory
    predictor = inference.create_predictor(config)

    # Process audio file
    input_wav_data = paddle.to_tensor([paddle.load_wav_file(audio_file)], dtype="float32")

    # Run inference
    input_tensor = predictor.get_input(0)
    input_tensor.set_data(input_wav_data)

    predictor.run()

    # Get the result
    output_tensor = predictor.get_output(0)
    result = output_tensor.numpy()[0]

    return result


def analyze_language_errors(text):
    # Initialize BERT model for language analysis
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased")

    # Tokenize and encode the text
    inputs = tokenizer(text, return_tensors="pt")

    # Perform inference with BERT
    outputs = model(**inputs)

    # Get the predicted class (0 for correct, 1 for incorrect)
    predicted_class = torch.argmax(outputs.logits, dim=1).item()

    return "Correct" if predicted_class == 0 else "Incorrect"


def main():
    # Replace with the path to your audio file
    audio_file = "E:/test.m4a"

    # Perform speech-to-text
    transcribed_text = speech_to_text(audio_file)
    print("Transcribed Text:", transcribed_text)

    # Analyze language errors with BERT
    language_analysis_result = analyze_language_errors(transcribed_text)
    print("Language Analysis Result:", language_analysis_result)


main()
