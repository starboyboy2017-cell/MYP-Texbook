# Chapter 8 · Sets and classification

*Text extract of the typeset pages (printed pages 130–145). The PDF is the authoritative edition. Letter-spaced display labels (part, chapter, stage and panel kickers) belong to the page design and are omitted from this extract.*

<!-- printed page 130 -->
A set is only a collection with a rule for belonging. Almost
every mathematical idea begins with deciding what belongs
together — and stating the rule precisely enough that
nothing slips in unnoticed.
What makes a classification useful rather than merely tidy, and who decides where the boundary lies?

<!-- printed page 131 -->
Statement of inquiry Classifying objects into sets with precisely stated rules reveals structure that is invisible when the objects are considered one at a time.
Key and related concepts
Key concept · Form. A set is defined by the form of its rule, not by the objects it happens to collect.
Related · Representation. Venn diagrams, set brackets and number-system trees are three representations of the
same relation.
Related · System. Number systems nest inside one another, and the nesting is itself a set relation.
Global context · Identities and relationships
Exploration: how a community sorts its own members — by age, by trade, by household — and what a sorting rule
includes and excludes.
Inquiry questions
– Factual: What does it mean for an element to belong to a set, and how is this written?
– Conceptual: Why does a precise rule matter more than a list?
– Debatable: Can any classification be neutral?
Criterion Strands Evidence in this chapter
A · Knowing and understanding i, ii, iii Use set notation accurately to describe a collection.
B · Investigating patterns i, ii, iii Find the pattern in the number of subsets of a set.
C · Communicating i, ii, iii, iv Draw a Venn diagram that another student can read correctly.
D · Applying mathematics i, ii, iii, iv Sort a real collection and justify the rule chosen.
ATL · Critical and creative thinking
In order for a student to classify without ambiguity, students must state the rule in a form that can be tested on a
borderline object.

<!-- printed page 132 -->
Everything in this room.
Sort everything in the room into two groups, then into three, then into five. Each time, write the rule you
used. Now swap rules with another group and try to sort by their rule without asking what it means.
A sorting hall is a classification made physical: the shelves encode a rule that customers are expected to infer.
Original illustration created for this edition.
One rule, two results.
Take the numbers from 1 to 20. Sort them using the rule “even”, then using the rule “multiple of 3”, then us-
ing both rules at once.
1. Which numbers appear in both groups?
2. Which numbers appear in neither group?
3. Does every number belong to at least one group this time? Try a different pair of rules where it does not.
4. Write a rule that puts every number 1–20 into exactly one group.
1–20 by two rules
11 12 13 14 15
16 17 18 19 20
shaded: even · outlined: multiple of 3 · both: darker F I G U R E 2 The numbers 1 to 20 arranged by two rules at once. The overlap is the set of numbers satisfying both.

<!-- printed page 133 -->
Classification needs a test
A classification is only as good as the test it implies. If you cannot say
whether a borderline object belongs, the rule is not yet precise enough.
8.1 Sets, elements and notation
Set and element
A set is a well-defined collection of objects. Each object in it is an ele-
ment (or member). We write x ∈ A to mean that x belongs to set A, and x
∉ A to mean that it does not.
Two ways to name a set
Method Example When to use it
Listing (roster) A = {2, 4, 6, 8} The set is small or finite.
Rule (set-builder) B = {x : x is an even number, 1 ≤ x ≤ 8}
The pattern is clear- er than the list.
Curly brackets always mean a set. Round brackets never do. The
colon in a rule reads “such that”, and the condition after it must be
precise enough to decide any candidate object.
P R O B L E M A = {2, 4, 6, 8, 10}. Decide whether each statement is true or false: 6 ∈ A, 7 ∈ A, 10 ∉ A.
1 6 is listed in A, so 6 ∈ A is true.
2 7 is not listed, so 7 ∈ A is false, which means 7 ∉ A is true.
3 10 is listed, so 10 ∉ A is false.
Every element of A satisfies the rule “even, between 1 and 11” ✓

<!-- printed page 134 -->
P R O B L E M Write the set of whole numbers between 5 and 15 that are divisible by 3, both by listing and by rule.
1 Candidates: 6, 9, 12, 15.
2 Listed: {6, 9, 12, 15}.
3 By rule: {x : x is a whole number, 5 < x ≤ 15, x is a multiple of 3}.
4 The rule must state the range as well as the property, or it de- scribes an infinite set.
Check the boundaries: 5 is excluded, 15 is included ✓
Confusing ∈ with ⊂
∈ compares an object with a set; ⊂ compares two sets. 3 ∈ {1, 2, 3} is
true, but {3} ⊂ {1, 2, 3} is a different statement about a set, not the num-
ber.
1. List the set of vowels in the word MATHEMATICS. F
2. Decide whether 12 ∈ {multiples of 4}. Explain. F
3. Write {3, 6, 9, 12} by rule. F
4. Write the set of even numbers from 2 to 12 by listing. F
5. Explain the difference between ∈ and ⊂. R
6. Write a rule that describes {1, 4, 9, 16, 25}. P
7. A set S = {x : x is a letter in BANANA}. List S and explain why it has fewer elements than the word has letters.
P
8. Find a rule that is precise for whole numbers but ambiguous for decimals, and explain the ambiguity.
E
8.2 Subsets, the universal set and the complement

<!-- printed page 135 -->
Subset, universal set, complement
A ⊂ B means every element of A is also in B. The universal set ξ is
everything under discussion. The complement A′ contains every ele-
ment of ξ that is not in A.
The universal set is a decision, not a fact. If ξ is the whole numbers,
the complement of the evens is the odds; if ξ is the digits 0–9, the com-
plement is {1, 3, 5, 7, 9}. Always state ξ before using a complement.
ξ
A′
A
F I G U R E 3 The shaded region is the complement of A inside the universal set ξ.
P R O B L E M List all subsets of {a, b}.
1 The empty set ∅ is a subset of every set.
2 Single-element subsets: {a}, {b}.
3 The whole set: {a, b}.
4 That is four subsets.
A N S W E R ∅, {a}, {b}, {a, b}.
A set with 2 elements has 22 = 4 subsets ✓
P R O B L E M ξ = {1, 2, 3, …, 12}, A = {multiples of 3}. List A and A′.
1 A = {3, 6, 9, 12}.
2 A′ contains everything in ξ not in A: {1, 2, 4, 5, 7, 8, 10, 11}.
3 Check that the two sets together give all twelve elements with no repeats.
A N S W E R A′ = {1, 2, 4, 5, 7, 8, 10, 11}
4 + 8 = 12 elements in total ✓

<!-- printed page 136 -->
1. Is {2, 4} a subset of {1, 2, 3, 4}? Explain. F
2. List all subsets of {p, q, r}. F
3. ξ = {1, …, 10}, A = {primes}. List A and A′. F
4. How many subsets has a set with 4 elements? F
5. Explain why the empty set is a subset of every set. R
6. Investigate the pattern in the number of subsets of a set with n elements and write the rule.
P
7. A class of 30 students is the universal set; 12 play football, 9 play chess. Explain why you cannot yet find the complement of the football players without more information.
E
8. Is every set a subset of itself? Justify your answer. E
8.3 Union, intersection and Venn diagrams
Union and intersection
The union A ∪ B contains everything in A or B or both. The intersection
A ∩ B contains only what is in both. Two sets with no common element
are disjoint.
A B
A B
A ∪ B   everything in either
A ∩ B   only what is in both
F I G U R E 4 Union and intersection shown on two identical circles. The shading, not the labels, carries the meaning.

<!-- printed page 137 -->
P R O B L E M In a class of 32, 18 study French, 15 study Spanish and 7 study both. Find the number who study at least one language and the number who study neither.
1 Both: 7.
2 French only: 18 − 7 = 11.
3 Spanish only: 15 − 7 = 8.
4 At least one: 11 + 7 + 8 = 26.
5 Neither: 32 − 26 = 6.
A N S W E R 26 study at least one; 6 study neither.
11 + 7 + 8 + 6 = 32, the whole class ✓
P R O B L E M A = {2, 4, 6, 8, 10} and B = {4, 8, 12}. Find A ∪ B and A ∩ B.
1 Intersection: elements in both — 4 and 8.
2 Union: everything in either, listed once — 2, 4, 6, 8, 10, 12.
3 Note that 4 and 8 appear once in the union, not twice.
A N S W E R A ∩ B = {4, 8}; A ∪ B = {2, 4, 6, 8, 10, 12}
|A| + |B| − |A ∩ B| = 5 + 3 − 2 = 6 = |A ∪ B| ✓
Adding the overlap twice
Adding 18 and 15 in Example 8.3.1 gives 33, which is larger than the
whole class. The seven students in both were counted twice; subtract
them once.
1. A = {1, 2, 3, 4}, B = {3, 4, 5}. Find A ∪ B and A ∩ B. F
2. In a group of 20, 12 like tea, 9 like coffee, 5 like both. How many like neither?
F
3. Draw a Venn diagram for two disjoint sets. F
4. C = {vowels}, D = {letters in MATHEMATICS}. Find C ∩ D. F
5. Explain why A ∩ B is always a subset of A. R
6. In a survey of 40 students, 25 walk to school, 18 cycle, 10 do both. Draw the diagram and find how many do neither.
P

<!-- printed page 138 -->
1. Two sets have 12 and 15 elements and their union has 20. Find the size of the intersection.
P
2. Investigate whether A ∪ B can ever have fewer elements than A. Explain using a diagram.
E
8.4 Classifying numbers and shapes
Sets give classification a language. The number systems from Chapter
1 nest inside one another, and each nesting is a subset relation that
can be drawn.
irrational numbers
Real numbers
Rational
nested subsets
Integer
Whole
Natural
F I G U R E 5 The number systems as nested sets. Every natural number is a whole number, every whole number an integer, and so on.
Classifying by more than one property
A quadrilateral can be classified by two independent properties: the
number of pairs of parallel sides, and whether the sides are equal. Draw-
ing the two properties as a two-way table reveals the categories and their
overlaps at the same time.
One pair parallel Two pairs parallel
All sides equal — rhombus (and square)
Opposite sides equal trapezium parallelogram / rectangle
No sides equal trapezium parallelogram

<!-- printed page 139 -->
P R O B L E M Place −5 in as many number sets as it belongs to.
1 −5 is an integer, because it is a whole number with a sign.
2 It is rational, because it can be written −5/1.
3 It is real. It is not natural or whole, because those sets start at 0 or 1.
Check each definition rather than the appearance of the number ✓
1. List the number sets to which 0 belongs. F
2. Is every square a rectangle? Explain using sets. F
3. Sort these into rational and irrational: 0.25, √2, 7, π, −3/4. F
4. Name the quadrilateral with two pairs of parallel sides and four right angles.
F
5. Explain why every natural number is an integer but not every in- teger is a natural number.
R
6. Draw a two-way table classifying triangles by angle type and by side equality.
P
7. Classify the numbers 1 to 20 by “prime” and “even” in a two-way table, and describe the empty cell.
P
8. Investigate whether a classification can be complete and non- overlapping at the same time, using shapes as an example.
E

<!-- printed page 140 -->
A set with one element has two subsets. Build sets of two, three and four elements, list every subset and
count them. Record the counts in a table and look for the pattern.
Elements Number of subsets Subsets
0 1 ∅
1 2 ∅, {a}
2 4 …
3 8 …
4 … …
Your investigation
1. Complete the table by listing, not by guessing.
2. Describe the pattern in the middle column as a rule involving n.
3. Explain why doubling happens each time a new element is added: what can you do with every existing
subset?
4. Predict the number of subsets of a five-element set and check by listing.
5. State the rule for the number of subsets of a set with n elements.
The result
A set with n elements has 2n subsets. Each element is either in or out of a given subset, so there are two independ-
ent choices per element.
ATL · Transfer
In order for a student to generalise, students must move from counting cases to explaining why the count doubles.

<!-- printed page 141 -->
A clinic records which of two services each patient used last month:
the general clinic (G) and the laboratory (L). In a sample of 60 pa-
tients, 38 used G, 27 used L and 15 used both. The clinic must justify
its staffing to a funding committee.
Your task
1. Draw a Venn diagram and fill in all four regions.
2. Find the number who used exactly one service.
3. Find the number who used neither, and explain what that group
could be.
4. Write two sentences the clinic director could use, each reporting a
different true number in a way that supports a different staffing
decision.
5. Explain why the same data can support two different conclusions.
6. State one way the survey could have produced misleading num-
bers.
Criterion D · strands i–iv
– Identify the given quantities and the universal set.
– Use the Venn diagram and subtraction as strategies.
– Apply the method accurately and check that the four regions
sum to 60.
– Evaluate how presentation of the same data changes its effect.
M I N I - TA S K The sorting rule
Context. Your class library needs re-shelving. The current rule “fic-
tion and non-fiction” no longer works for the collection.

<!-- printed page 142 -->
1. Collect or imagine 20 items. State a sorting rule with two proper-
ties.
2. Draw the two-way table and place every item.
3. Identify any item that is hard to place and explain why.
4. Revise the rule so that the difficult item can be placed.
5. Test the revised rule on a classmate's item list.
6. Evaluate: which rule produced fewer empty cells, and did that
make it a better classification?
Criteria and strands developed
– Criterion B · Investigating patterns — i–iii: the pattern in the
number of subsets.
– Criterion C · Communicating — i–iv: table clarity, notation and
justification of the rule.
One property runs across the top, the other runs down the side.
Fiction Not fiction
12 novels 4 atlases Hardback
9 short-story collections 3 dictionaries Paperback
Each cell is the intersection of the two properties. Every one of the 28 items lands in exactly one cell; an item that fits none tells you the rule needs revising.
F I G U R E 6 A two-property classification drawn as a table: each cell is an intersection of the two rules.
An empty cell is evidence
A cell with no items is not a failure: it says no object in your collection
satisfies both properties. Ask whether the property is badly chosen or
the collection is genuinely limited, and say which in your write-up.
Before you hand this in
– Name both properties in the table heading.
– The four cell counts must add to the total.
– Show where your revised rule puts the awkward item.
– Say what the table revealed that a list would hide.

<!-- printed page 143 -->
What this chapter established
– A set is defined by a rule, and ∈ tests membership of elements.
– Curly brackets name sets; the colon in a rule reads “such that”.
– A ⊂ B, the universal set ξ and the complement A′ extend set vocabulary.
– A ∪ B and A ∩ B describe everything-in-either and everything-in-both.
– A set with n elements has 2n subsets.
Vocabulary
Term Meaning
element An object belonging to a set.
subset A set all of whose elements lie in another set.
universal set ξ Everything under discussion in a particular problem.
complement The elements of ξ that are not in the set.
union Everything in either set, listed once.
intersection Only the elements in both sets.
disjoint Having no elements in common.
empty set ∅ The set with no elements; a subset of every set.
Misconceptions to watch
Three that persist
– A list is a set. {1, 2, 2, 3} is the set {1, 2, 3}: repeats collapse.
– ∈ and ⊂ are interchangeable. They compare an object with a set and a set with a set.
– Sets are always numbers. A set can contain letters, shapes or people.

<!-- printed page 144 -->
Self-assessment
I can … Not yet Getting there
Confident
read and write set notation □ □ □
list subsets of a set □ □ □
use a universal set and complement □ □ □
find unions and intersections □ □ □
complete a Venn diagram from a word problem
□ □ □
justify a classification rule □ □ □
Reflect on the criteria
– Criterion A: which calculation in this chapter would you now do
without checking?
– Criterion C: where did notation or a diagram carry an argument
for you?
– Criterion D: which real context changed how you understood the
mathematics?
ATL · Reflection
In order for a student to state a rule, students must test it against one ob-
ject that does and one that does not belong.
Looking ahead · Chapter 9 · Perimeter, area and surface area takes
these ideas further. The self-assessment above tells you which to re-
visit first.
A note to your teacher
Two sentences: what you can now do that you could not do at the start
of the chapter, and which single idea you would still like explained.

<!-- printed page 145 -->
1. List the set of factors of 12. F
2. Is 15 ∈ {multiples of 5}? Explain. F
3. Write {1, 8, 27, 64} by rule. F
4. How many subsets has a set with 5 elements? F
5. ξ = {1, …, 9}, A = {1, 3, 5, 7, 9}. List A′. F
6. Explain what a universal set is and why it must be stated. R
7. A = {2, 3, 5, 7}, B = {1, 2, 3, 4}. Find A ∪ B and A ∩ B. R
8. In a group of 50, 30 read the newspaper, 22 read magazines, 12 read both. Draw the diagram and find the number who read neither.
P
9. A set has 64 subsets. How many elements has it? P
10. Explain why a Venn diagram with two circles has four regions, and draw a third circle to show how many regions appear.
P
11. Sort the numbers 1 to 30 by the properties “prime” and “multiple of 3” in a two-way table. P
12. A survey of 40 people asked whether they owned a bicycle (B) and a helmet (H). 22 had B, 18 had H and 10 had neither. Find how many had both.
E
13. Investigate whether the number of regions in a Venn diagram with n circles follows a simple rule, testing up to three circles.
E
14. Design a classification of the quadrilaterals in this chapter using two properties, and state which cells are empty and why.
E
Question If you cannot do this …
1–5 Revisit 8.1 and 8.2: rule first, list second.
6–7 Revisit 8.3: name each region before adding.
8–11 Revisit 8.3 and the investigation: fill the overlap first.
12–14 Revisit 8.4: two properties give a table, not a list.

