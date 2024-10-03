import torch;
import fam.llm.fast_inference as fast_infer;

device = torch.device("cuda")
tts = fast_infer.TTS()