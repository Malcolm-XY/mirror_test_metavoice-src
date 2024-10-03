import torch;
import torch._dynamo;
import fam.llm.fast_inference as fast_infer;

torch._dynamo.config.suppress_errors = True
tts = fast_infer.TTS()