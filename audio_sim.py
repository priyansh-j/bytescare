import librosa
import numpy as np

# Load audio files
a1 = input("Enter the location of the first audio file: ")
a2 = input("Enter the location of the second audio file: ")

audio1, sr1 = librosa.load(a1)
audio2, sr2 = librosa.load(a2)

# Extract audio features
mfcc1 = librosa.feature.mfcc(y=audio1,sr=sr1)
mfcc2 = librosa.feature.mfcc(y=audio2,sr=sr2)

min_length = min(mfcc1.shape[1], mfcc2.shape[1])
mfcc1 = mfcc1[:, :min_length]
mfcc2 = mfcc2[:, :min_length]

# Compute similarity using cosine similarity
similarity = np.dot(mfcc1.flatten(), mfcc2.flatten()) / (np.linalg.norm(mfcc1) * np.linalg.norm(mfcc2))

# Print similarity percentage
print("Similarity percentage:", similarity * 100)
