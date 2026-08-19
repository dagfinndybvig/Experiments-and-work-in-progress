# Neuro-Symbolic Library Sorting System: Implementation Plan

*Applying the neuro-symbolic architecture to a real workplace challenge at a hypothetical library*

---

## Overview

This document outlines how the neuro-symbolic AI architecture demonstrated in this repository could be deployed to solve a concrete workplace problem: **automated, reliable sorting of library materials**. The same principles that power the demo systems — combining natural language understanding with formal constraint satisfaction — provide a robust solution for library operations where **precision, accountability, and verifiability** are paramount.

---

## The Problem: Library Sorting

Library sorting presents a classic challenge that aligns perfectly with neuro-symbolic strengths:

- **Formal constraints**: Dewey Decimal classification, shelf capacities, material types, collection rules
- **Natural language interface**: Staff instructions like "sort these by date, but keep rare manuscripts separate"
- **Critical reliability**: Patrons must be able to find materials; misplaced items are effectively lost
- **Edge cases**: Conflicting rules, capacity limits, special collections requiring separate handling

A pure LLM approach would be unreliable (hallucinating placements) and unauditable. A pure rule-based system would be brittle (unable to handle novel instructions). The neuro-symbolic loop combines the best of both.

---

## Architecture

The system follows the same **Discourse + Geometry** pattern as the demonstration code:

```
┌─────────────────────────────────────────────────────────┐
│           NEURO-SYMBOLIC LIBRARY SORTER                   │
├─────────────────────────────┬─────────────────────────────┤
│         DISCOURSE             │           GEOMETRY          │
│  ┌─────────────────────┐    │    ┌─────────────────────┐    │
│  │ Small LLM           │    │    │ SWI-Prolog Engine   │    │
│  │ - Interpret staff   │────┼───►│ - Classification     │    │
│  │   instructions      │    │    │   rules             │    │
│  │ - Formalize to      │    │    │ - Physical          │    │
│  │   Prolog clauses    │    │    │   constraints        │    │
│  │ - Reinterpret       │    │    │ - Verification       │    │
│  │   results           │    │    └─────────────────────┘    │
│  └─────────────────────┘    │                                 │
└─────────────────────────────┴─────────────────────────────┘
```

### Components

| Component | Technology | Role | Source File Reference |
|-----------|------------|------|----------------------|
| Discourse | Small LLM (e.g., qwen2.5:7b via Ollama) or regex fallback | Natural language understanding, formalization | `neuro_symbolic_demo_ollama.py:OllamaDiscourse` |
| Geometry | SWI-Prolog via pyswip | Constraint satisfaction, verification | `neuro_symbolic_demo_prolog.py:PrologEngine` |
| Loop orchestrator | Python | Manages the neuro-symbolic cycle | `neuro_symbolic_demo.py:NeuroSymbolicSystem` |

---

## Implementation: Library-Specific Rules

### Step 1: Knowledge Base (Geometry Component)

The Prolog knowledge base encodes all library sorting constraints:

```prolog
% ============================================
% PHYSICAL LAYOUT
% ============================================

% Shelves with capacities and locations
shelf(a, capacity=50, location=main_room, floor=1, section='A').
shelf(b, capacity=100, location=main_room, floor=1, section='B').
shelf(rare, capacity=20, location=archive, floor=2, climate_controlled=true).
shelf(oversize, capacity=30, location=basement, floor=0).

% ============================================
% CLASSIFICATION SCHEMES
% ============================================

% Dewey Decimal ranges
dewey_range(philosophy, 100, 199).
dewey_range(science, 500, 599).
dewey_range(technology, 600, 699).
dewey_range(history, 900, 999).

% Library of Congress (alternative)
loc_range(philosophy, 'B').
loc_range(science, 'Q').
loc_range(technology, 'T').

% ============================================
% MATERIAL TYPES AND COLLECTIONS
% ============================================

material_type(Book, standard) :- 
    not(rare_manuscript(Book)),
    not(oversize(Book)).

rare_manuscript(Book) :-
    age(Book, Years),
    Years > 150,
    condition(Book, fragile).

oversize(Book) :-
    dimensions(Book, Width, Height, _),
    (Width > 30 ; Height > 40).

special_collection(Book, rare) :- rare_manuscript(Book).
special_collection(Book, oversize) :- oversize(Book).
special_collection(Book, none) :- material_type(Book, standard).

% ============================================
% SORTING RULES
% ============================================

% Primary sorting by classification
sort_order(Book1, Book2, before) :-
    dewey_number(Book1, D1),
    dewey_number(Book2, D2),
    D1 < D2.

sort_order(Book1, Book2, before) :-
    loc_class(Book1, C1),
    loc_class(Book2, C2),
    class_precedes(C1, C2).

% Secondary sorting: publication date
sort_order(Book1, Book2, before) :-
    same_class(Book1, Book2),
    publication_date(Book1, Date1),
    publication_date(Book2, Date2),
    Date1 < Date2.

% Collection separation rules
must_separate(Book1, Book2) :-
    special_collection(Book1, rare),
    special_collection(Book2, C),
    C \= rare.

must_separate(Book1, Book2) :-
    special_collection(Book1, oversize),
    special_collection(Book2, C),
    C \= oversize.

% Shelf assignment
assign_to_shelf(Book, Shelf) :-
    special_collection(Book, rare),
    shelf(Shelf, climate_controlled=true),
    shelf_remaining_capacity(Shelf, Remaining),
    Remaining > 0.

assign_to_shelf(Book, Shelf) :-
    special_collection(Book, oversize),
    shelf(Shelf, section=oversize),
    shelf_remaining_capacity(Shelf, Remaining),
    Remaining > 0.

assign_to_shelf(Book, Shelf) :-
    special_collection(Book, none),
    shelf(Shelf, climate_controlled=false),
    shelf(Shelf, section=S),
    dewey_range(Category, Low, High),
    dewey_number(Book, D),
    between(Low, High, D),
    section_matches_category(S, Category),
    shelf_remaining_capacity(Shelf, Remaining),
    Remaining > 0.

% ============================================
% VERIFICATION RULES
% ============================================

valid_placement(Placements) :-
    % All books are placed
    findall(Book, book(Book), AllBooks),
    placed_books(Placements, Placed),
    sort(AllBooks, SortedAll),
    sort(Placed, SortedPlaced),
    SortedAll = SortedPlaced,
    % No constraint violations
    no_separation_violations(Placements),
    no_capacity_violations(Placements),
    % Sorting order is maintained
    ordered_by_classification(Placements).

no_separation_violations(Placements) :-
    forall((member(book(B1, _), Placements),
            member(book(B2, _), Placements),
            must_separate(B1, B2)),
           (shelf_for_book(B1, Placements, S1),
            shelf_for_book(B2, Placements, S2),
            S1 \= S2)).

no_capacity_violations(Placements) :-
    forall(shelf(S, capacity=C),
           (count_books_on_shelf(S, Placements, Count),
            Count =< C)).
```

### Step 2: Discourse Layer (Natural Language Interface)

The LLM (or regex fallback) handles staff instructions:

```python
class LibraryDiscourse(LLMDiscourse):
    """Specialized for library sorting instructions."""
    
    def __init__(self, prolog_engine):
        super().__init__(prolog_engine)
        self._init_library_domain_knowledge()
    
    def _init_library_domain_knowledge(self):
        self.domain_knowledge['library'] = {
            'interpreters': {
                r'(?i)sort\s+by\s+(dewey|decimal|call\s+number)':
                    lambda m: "sort_criteria(dewey).",
                r'(?i)sort\s+by\s+publication\s+(date|year)':
                    lambda m: "sort_criteria(date).",
                r'(?i)sort\s+by\s+author':
                    lambda m: "sort_criteria(author).",
                r'(?i)keep\s+(rare|manuscript|special)\s+books\s+separate':
                    lambda m: "separation_rule(rare, separate).",
                r'(?i)(oversize|large)\s+books\s+on\s+shelf\s+(\w+)':
                    lambda m: f"assign_collection(oversize, {m.group(2)}).",
                r'(?i)put\s+(all|the)\s+(\w+)\s+books\s+in\s+section\s+(\w+)':
                    lambda m: f"assign_category({m.group(2).lower()}, {m.group(3)}).",
            },
            'reinterpreters': {
                'true': 'All books sorted according to constraints.',
                'false': 'Cannot sort: constraint violation detected.',
            }
        }
```

### Step 3: The Neuro-Symbolic Sorting Loop

```python
def sort_library_materials(books, instruction):
    """Complete sorting cycle for library materials."""
    
    system = NeuroSymbolicSystem()
    
    # Step 1-2: Interpret and Formalize
    discourse = LibraryDiscourse(system.geometry)
    formal_rules = discourse.formalize(instruction, domain='library')
    
    # Load book data into Prolog
    for book in books:
        system.geometry.add_fact(f"book({book.id}).")
        system.geometry.add_fact(f"dewey_number({book.id}, {book.dewey}).")
        system.geometry.add_fact(f"publication_date({book.id}, {book.date}).")
        # ... other book properties
    
    # Step 3: Derive
    query = "valid_placement(Placements)."
    solutions = system.geometry.query(query)
    
    # Step 4: Verify
    if not solutions:
        # Try to identify the constraint violation
        diagnostics = diagnose_failure(system.geometry)
        return {
            'status': 'failed',
            'reason': diagnostics,
            'suggestions': generate_suggestions(diagnostics)
        }
    
    # Step 5: Reinterpret
    placement = solutions[0]  # Get the valid placement
    natural_language_summary = discourse.reinterpret(
        solutions, 
        f"Sorted {len(books)} books according to: {instruction}"
    )
    
    return {
        'status': 'success',
        'placement': placement,
        'summary': natural_language_summary
    }
```

---

## Deployment Workflow

### 1. Setup

```bash
# Install dependencies (same as neuro_symbolic_demo_prolog.py)
pip install pyswip requests

# Install SWI-Prolog
# Windows: winget install SWI-Prolog.SWI-Prolog
# macOS: brew install swi-prolog
# Linux: sudo apt install swi-prolog

# Optional: Install Ollama for LLM Discourse
# winget install Ollama.Ollama  # Windows
# brew install ollama            # macOS
ollama pull qwen2.5:7b
```

### 2. Integration with Library Systems

```python
# Example: CSV import of new acquisitions
import csv
from library_sorter import sort_library_materials

with open('new_acquisitions.csv') as f:
    books = list(csv.DictReader(f))

result = sort_library_materials(
    books,
    "Sort by Dewey number, but keep rare manuscripts on shelf A"
)

if result['status'] == 'success':
    generate_shelf_labels(result['placement'])
    update_catalog(result['placement'])
else:
    flag_for_manual_review(result)
```

### 3. Fallback Modes

| Mode | LLM Available | Prolog Available | Behavior |
|------|---------------|------------------|----------|
| Full | ✅ | ✅ | LLM interprets, Prolog sorts |
| Prolog-only | ❌ | ✅ | Regex interprets, Prolog sorts |
| Degraded | ✅ | ❌ | LLM interprets, toy engine sorts (limited) |
| Minimal | ❌ | ❌ | Regex interprets, toy engine sorts |

---

## Advantages Over Traditional Approaches

| Approach | Flexibility | Reliability | Auditability | Cost |
|----------|-------------|-------------|--------------|------|
| Pure LLM | High | Low | Low | Medium |
| Traditional rules engine | Low | High | Medium | Low |
| **Neuro-symbolic** | **High** | **High** | **High** | **Low** |

### Specific Benefits for the Library

1. **Staff Empowerment**: Library staff can use natural language instructions without learning Prolog syntax
2. **Precision**: Guaranteed correct placement according to all constraints
3. **Accountability**: Every placement decision is verifiable against the rules
4. **Adaptability**: New sorting rules can be added by updating the Prolog knowledge base
5. **Error Handling**: Failures are explicit and diagnostic, not silent
6. **Resource Efficiency**: Runs on modest hardware (Raspberry Pi + small LLM)

---

## Workplace Integration



This system could be integrated into daily operations:

- **Acquisitions processing**: Automatically sort new arrivals according to collection policies
- **Returns reshelving**: Verify returned items go to correct locations
- **Collection reorganization**: Model and validate large-scale reshelving projects before execution
- **Training tool**: Help new staff understand sorting rules through interactive queries
- **Portable**: With the simple hardware requirements it could even be a handheld system.

### Implementation Roadmap

| Phase | Task | Timeline | Dependencies |
|-------|------|----------|--------------|
| 1 | Adapt demo PrologEngine for library domain | 1 week | None |
| 2 | Develop library-specific Discourse layer | 1 week | Phase 1 |
| 3 | Integrate with existing catalog system | 2 weeks | Phases 1-2 |
| 4 | Test with sample data sets | 1 week | Phases 1-3 |
| 5 | Deploy to acquisitions workflow | 1 week | All previous |
| 6 | Expand to other library operations | Ongoing | Phase 5 |

### Cost Estimate

- **Hardware**: Existing library computers sufficient; optionally ~$500 for dedicated Raspberry Pi cluster.
- **Software**: Free/open source (SWI-Prolog, Python, pyswip)
- **LLM**: Optional; can run without or with local small models (no API costs)
- **Development**: ~6 weeks of part-time development

---

## Conclusion

The neuro-symbolic approach transforms library sorting from a **manual, error-prone process** into a **reliable, auditable, and flexible system**. By combining the natural language understanding of LLMs (or even simple regex patterns) with the formal reasoning power of Prolog, a library could achieve **higher accuracy with lower cognitive load on staff** — a perfect example of how these philosophical insights about intelligence translate into practical workplace solutions.

The code in this repository already implements 90% of the required infrastructure. Adapting it for library sorting would be a **straightforward application** of the existing neuro-symbolic framework to a specific domain.

---

## See Also

- [Neuro-Symbolic AI Demonstration Guide](NEURO_SYMBOLIC_DEMO_GUIDE.md) — Full technical documentation of the underlying architecture
- [From Plato to Prolog to Prompts](From_Plato_to_Prolog_to_Prompts.md) — Philosophical foundation for this approach
- [neuro_symbolic_demo_prolog.py](neuro_symbolic_demo_prolog.py) — The Prolog engine implementation (directly reusable)
- [neuro_symbolic_demo_ollama.py](neuro_symbolic_demo_ollama.py) — LLM integration example (optional for library use)
