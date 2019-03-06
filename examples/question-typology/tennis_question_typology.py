# This example extracts question types from the Wimbledon Winner Interviews Dataset explained TODO
#   using the methods in the asking too much paper (http://www.cs.cornell.edu/~cristian/Asking_too_much.html) to extract question types.
#   (since there is a seed provided, multiple executions of this script will always produce the same clusters)

from convokit import Corpus, Parser, QuestionTypology, download

print("Loading tennis dataset...")
corpus = Corpus(filename=download("tennis-corpus"))

# Get parses for each utterance in the Corpus. This step is needed since the
# QuestionTypology will use the parses in its computation.
parser = Parser()
corpus = parser.fit_transform(corpus)

# initialize the QuestionTypology Transformer. Note the following differences 
# from the original tennis_question_typology.py:
#  - We do not pass in a corpus, as the Transformer-based API will
#    instead be having us apply the QuestionTypology to a corpus
#    after initialization
#  - We do not pass in a dataset name, for the same reason as above
#  - We do not pass in a data_dir, as serialization is now manual
questionTypology = QuestionTypology(num_dims=25, num_clusters=8, verbose=10000, random_seed=125)

print("Fitting QuestionTypology...")
corpus = questionTypology.fit_transform(corpus)

questionTypology.display_totals()
print("10 examples for types 1-8:")
for i in range(8):
    questionTypology.display_motifs_for_type(i, num_egs=10)
    questionTypology.display_answer_fragments_for_type(i, num_egs=10)
    questionTypology.display_question_answer_pairs_for_type(corpus, i, num_egs=10)
