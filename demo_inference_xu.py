import torch;
import torch._dynamo
import fam.llm.inference as infer;

torch._dynamo.config.suppress_errors = True
Model = infer.Model()