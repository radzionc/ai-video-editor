import stable_whisper

def transcribe(input_path):
  model = stable_whisper.load_model('base')
  
  result = model.transcribe(input_path, regroup=False)
  (
    result
    .clamp_max()
    .split_by_punctuation([('.', ' '), '。', '?', '？', (',', ' '), '，'])
    .split_by_gap(.8)
    .merge_by_gap(.6)
    .split_by_punctuation([('.', ' '), '。', '?', '？'])
  )
  return result