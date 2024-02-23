
# NPL EDU JAD

## Install Gram

To utilize the Gram language correction tool, follow these steps for installation:

0. Install the SpeechRecognition package:
   ```shell
   pip install SpeechRecognition
   ```
1. create a virtual environment

2. go to command prompt

3. Enter the following commands: 

```shell
python3 -m venv my_venv

pip install numpy scipy torch transformers tqdm

pip3 install torch torchvision torchaudio

pip install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git

python -m spacy download en_core_web_sm
```

Optionally, try to install the Gramformer package manually.

Now, enjoy :)
