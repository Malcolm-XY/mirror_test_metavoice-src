import torch;
import fam.llm.fast_inference as fast_infer;

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tts = fast_infer.TTS()