% COVID DIAGNOSIS

% Dynamic predicates for tests and their results
:- dynamic test/2.
:- dynamic symptom/1.

% Facts about symptoms
symptom(fever).
symptom(headache).
symptom(fatigue).
symptom(short_breath).
symptom(muscle_pain).

% Rules for diagnosing covid based on test results
diagnose_covid(TestResult) :-
    symptom(fever),
    symptom(headache),
    symptom(fatigue),
    symptom(sweating),
    symptom(short_breath),
    symptom(muscle_pain),
    test(microscopic_examination, positive),
    test(rapid_diagnostic_test, positive),
    test(pcr, positive),
    !, % Cut operator to prevent backtracking
    write('You have Covid.'),
    TestResult = positive.

diagnose_covid(TestResult) :-
    write('You have No Covid Detected.'),
    TestResult = negative.


% Main predicate to start the diagnosis
start_diagnosis :-
    write('Covid Diagnosis Program'), nl,
    write('Please enter the symptoms:'), nl,
    ask_symptoms,
    write('Please enter the test results:'), nl,
    ask_test_results(TestResult),
    write('------------------------------------------'), nl,
    write('Final diagnosis:'), nl,
    diagnose_covid(TestResult).

% Predicate to ask for symptoms
ask_symptoms :-
    write('Do you have fever? (yes/no)'),
    read(Response1),
    (Response1 = yes -> assert(symptom(fever)) ; assertz(symptom(fever))),

    write('Do you have headache? (yes/no)'),
    read(Response2),
    (Response2 = yes -> assert(symptom(headache)) ; assertz(symptom(headache))),

    write('Do you have fatigue? (yes/no)'),
    read(Response3),
    (Response3 = yes -> assert(symptom(fatigue)) ; assertz(symptom(fatigue))),

    write('Do you have sweating? (yes/no)'),
    read(Response4),
    (Response4 = yes -> assert(symptom(sweating)) ; assertz(symptom(sweating))),

    write('Do you have problem of short breath? (yes/no)'),
    read(Response5),
    (Response5 = yes -> assert(symptom(short_breath)) ; assertz(symptom(short_breath))),

    write('Do you have muscle pain? (yes/no)'),
    read(Response6),
    (Response6 = yes -> assert(symptom(muscle_pain)) ; assertz(symptom(muscle_pain))),

    !. % Cut operator to prevent backtracking

ask_symptoms.

% Predicate to ask for test results
ask_test_results(TestResult) :-
    write('Is the microscopic examination test result positive? (yes/no)'),
    read(Response),
    (Response = yes -> assert(test(microscopic_examination, positive)) ; assert(test(microscopic_examination, negative))),

    write('Is the rapid diagnostic test result positive? (yes/no)'),
    read(Response2),
    (Response2 = yes -> assert(test(rapid_diagnostic_test, positive)) ; assert(test(rapid_diagnostic_test, negative))),

    write('Is the PCR test result positive? (yes/no)'),
    read(Response3),
    (Response3 = yes -> assert(test(pcr, positive)) ; assert(test(pcr, negative))),

    TestResult = Response3.
