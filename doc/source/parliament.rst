Parliament Question Time Corpus
===============================

A collections of questions and answers from parliamentary question periods in the British House of Commons from May 1979 to December 2016 (433,787 utterances). 

Distributed together with:
`Asking Too Much? The Rhetorical Role of Questions in Political Discourse <https://www.cs.cornell.edu/~cristian/Asking_too_much.html>`_. Justine Zhang, Arthur Spirling, Cristian Danescu-Niculescu-Mizil. EMNLP 2017.


Dataset details
---------------

Speaker-level information
^^^^^^^^^^^^^^^^^^^^^^^^^

The speakers in the dataset are members of the Parliament. For each speaker, the dataset further includes the following metadata:

* name: name of the speaker
* member_start: start time of the speaker as the member of the Parliament
* member_end: end time of the speaker as the member of the Parliament
* changed_parties: whether the speaker has changed parties
* first_party: first party the speaker is affiliated with
* last_party: last party the speaker is affiliated with


Utterance-level information
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each question or answer is viewed as an utterance. For each utterance, we provide:

* id: index of the utterance
* speaker: the speaker who authored the utterance
* conversation_id: id of the first utterance in the conversation this utterance belongs to
* reply_to: id of the utterance to which this utterance replies to (None if the utterance is not a reply)
* timestamp: time of the utterance
* text: textual content of the utterance

Additional metadata include:

* is_question: whether the utterance is a question
* is_answer: whether the utterance is an answer to a question
* pair_idx: index of the question-answer pair
* is_incubent: whether the speaker is an Incumbent
* is_minister: whether the speaker is a Minister
* is_oppn: whether the speaker is from the opposition party
* party: party affiliation of the speaker
* parsed: parsed version of the utterance text, represented as a SpaCy Doc


Usage
-----

To download directly with ConvoKit: 

>>> from convokit import Corpus, download
>>> corpus = Corpus(filename=download("parliament-corpus"))


For some quick stats:

>>> corpus.print_summary_stats()
Number of Speakers: 1978
Number of Utterances: 433787
Number of Conversations: 216894


Additional note
---------------

See this `example notebook <https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/question-typology/parliament_questions_example.ipynb>`_. for an example of how to group questions in this dataset according to their rhetorical roles.  
