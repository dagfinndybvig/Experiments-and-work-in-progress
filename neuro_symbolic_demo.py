#!/usr/bin/env python3
"""
Neuro-Symbolic AI Demonstration: From Plato to Prolog to Prompts
================================================================

This script demonstrates the neuro-symbolic architecture described in the essay
"From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason."

The system implements the loop:
    Interpret (LLM/Discourse) -> Formalize (LLM) -> Derive (Prolog/Geometry) 
    -> Verify (Prolog) -> Reinterpret (LLM) -> Revise (Loop)

Components:
- Discourse: Simulated LLM that interprets natural language and generates formal representations
- Geometry: Simple Prolog-like engine that performs formal reasoning

Example domains:
1. Classical logic (Aristotle's syllogisms)
2. Family relationships (ontology)
3. Planning/logistics (constraint reasoning)
4. Legal reasoning (expert systems)
"""

import re
from collections import defaultdict
from typing import List, Dict, Tuple, Optional, Set


# ============================================================================
# GEOMETRY: Simple Prolog-like Logic Engine
# ============================================================================

class PrologEngine:
    """
    A simple Prolog-like logic programming engine.
    
    This is the 'Geometry' component - the formal system that performs
    structured reasoning according to formal rules.
    
    Implements:
    - Facts: ground truths (e.g., parent(john, mary))
    - Rules: logical implications (e.g., ancestor(X, Y) :- parent(X, Y))
    - Queries: questions to the knowledge base (e.g., ancestor(X, mary)?)
    - Backward chaining: goal-directed reasoning
    """
    
    def __init__(self):
        self.facts = set()
        self.rules = []
        self.builtins = {
            '=': self._builtin_equals,
            '!=': self._builtin_not_equals,
            '<': lambda a, b: float(a) < float(b) if self._is_numeric(a) and self._is_numeric(b) else False,
            '>': lambda a, b: float(a) > float(b) if self._is_numeric(a) and self._is_numeric(b) else False,
            'is': self._builtin_is,
        }
    
    def _is_numeric(self, term):
        try:
            float(term)
            return True
        except (ValueError, TypeError):
            return False
    
    def _builtin_equals(self, a, b):
        return a == b
    
    def _builtin_not_equals(self, a, b):
        return a != b
    
    def _builtin_is(self, expr, value):
        """Simple arithmetic evaluation"""
        try:
            # Evaluate simple expressions like X is 2 + 3
            parts = expr.split()
            if len(parts) == 3 and parts[1] == '+':
                result = float(parts[0]) + float(parts[2])
                return result == float(value)
            elif len(parts) == 3 and parts[1] == '-':
                result = float(parts[0]) - float(parts[2])
                return result == float(value)
            elif len(parts) == 1:
                return float(parts[0]) == float(value)
            return False
        except:
            return False
    
    def add_fact(self, fact: str):
        """Add a fact to the knowledge base"""
        fact = fact.strip()
        if fact and not fact.startswith('%') and not fact.startswith('/*'):
            # Normalize: remove trailing period if present
            fact = fact.rstrip('.')
            self.facts.add(fact)
    
    def add_rule(self, rule: str):
        """Add a rule to the knowledge base"""
        rule = rule.strip()
        if rule and not rule.startswith('%') and not rule.startswith('/*'):
            # Convert rule from "head :- body." to (head, [body1, body2, ...])
            if ':-' in rule:
                head_part, body_part = rule.split(':-', 1)
                head = head_part.strip().rstrip('.')
                # Parse body atoms properly, handling commas inside parentheses
                body_atoms = self._parse_body(body_part)
                self.rules.append((head, body_atoms))
    
    def _parse_body(self, body_str: str) -> List[str]:
        """Parse a rule body into individual atoms, handling commas inside parentheses or lists"""
        atoms = []
        current = []
        depth = 0
        for char in body_str:
            if char in '([':
                depth += 1
                current.append(char)
            elif char in ')]':
                depth -= 1
                current.append(char)
            elif char == ',' and depth == 0:
                # Comma at top level - split here
                atom = ''.join(current).strip().rstrip('.')
                if atom:
                    atoms.append(atom)
                current = []
            else:
                current.append(char)
        # Add the last atom
        if current:
            atom = ''.join(current).strip().rstrip('.')
            if atom:
                atoms.append(atom)
        return atoms
    
    def load_program(self, program: str):
        """Load a complete Prolog program"""
        self.facts.clear()
        self.rules.clear()
        
        for line in program.split('\n'):
            line = line.strip()
            if not line or line.startswith('%') or line.startswith('/*'):
                continue
            if ':-' in line:
                self.add_rule(line)
            elif line.endswith('.'):
                self.add_fact(line)
            elif line:  # facts without period
                self.add_fact(line + '.')
    
    def _match(self, pattern: str, fact: str) -> Dict[str, str]:
        """
        Try to match a pattern against a fact, returning variable bindings.
        Pattern: predicate(Arg1, Arg2, ...)
        Fact: predicate(Value1, Value2, ...)
        """
        # Extract predicate name and arguments
        pattern_pred, pattern_args = self._parse_term(pattern)
        fact_pred, fact_args = self._parse_term(fact)
        
        if pattern_pred != fact_pred:
            return None
        
        if len(pattern_args) != len(fact_args):
            return None
        
        bindings = {}
        for pat_arg, fact_arg in zip(pattern_args, fact_args):
            # Check if pattern argument is a variable (starts with uppercase)
            if pat_arg[0].isupper():
                # Variable: bind it to the fact argument
                if pat_arg in bindings:
                    if bindings[pat_arg] != fact_arg:
                        return None  # Inconsistent binding
                else:
                    bindings[pat_arg] = fact_arg
            else:
                # Constant: must match exactly
                if pat_arg != fact_arg:
                    return None
        
        return bindings
    
    def _match_with_bindings(self, head: str, goal: str, current_bindings: Dict[str, str]) -> Optional[Dict[str, str]]:
        """
        Match a rule head against a goal, considering current bindings.
        This handles the case where the goal has already-bound variables.
        Returns new bindings that extend current_bindings.
        """
        # Parse both head and goal
        head_pred, head_args = self._parse_term(head)
        goal_pred, goal_args = self._parse_term(goal)
        
        if head_pred != goal_pred:
            return None
        
        if len(head_args) != len(goal_args):
            return None
        
        # Try to match arguments
        new_bindings = current_bindings.copy()
        for head_arg, goal_arg in zip(head_args, goal_args):
            # Resolve both arguments with current bindings
            head_resolved = self._resolve(head_arg, current_bindings)
            goal_resolved = self._resolve(goal_arg, current_bindings)
            
            # Check if both are variables
            head_is_var = head_resolved[0].isupper()
            goal_is_var = goal_resolved[0].isupper()
            
            if head_is_var and goal_is_var:
                # Both are variables - they must be the same variable name
                if head_resolved != goal_resolved:
                    # Different variables - need to check if they're bound
                    # If head_resolved is bound, goal_resolved must match
                    if head_resolved in new_bindings:
                        if new_bindings[head_resolved] != goal_resolved:
                            return None
                    elif goal_resolved in new_bindings:
                        # Bind head to whatever goal is bound to
                        new_bindings[head_resolved] = new_bindings[goal_resolved]
                    else:
                        # Both unbound variables with different names
                        # This is a most general unifier situation
                        # For simplicity, bind them together
                        new_bindings[head_resolved] = goal_resolved
            elif head_is_var:
                # head_arg is a variable, goal_resolved is a constant or bound var
                if head_resolved in new_bindings:
                    if new_bindings[head_resolved] != goal_resolved:
                        return None  # Inconsistent
                else:
                    new_bindings[head_resolved] = goal_resolved
            elif goal_is_var:
                # goal_arg is a variable, head_resolved is a constant
                if goal_resolved in new_bindings:
                    if new_bindings[goal_resolved] != head_resolved:
                        return None
                else:
                    new_bindings[goal_resolved] = head_resolved
            else:
                # Both are constants
                if head_resolved != goal_resolved:
                    return None
        
        return new_bindings
    
    def _parse_term(self, term: str) -> Tuple[str, List[str]]:
        """Parse a term like predicate(arg1, arg2) into (predicate, [arg1, arg2])"""
        term = term.strip().rstrip('.')
        if '(' in term and term.endswith(')'):
            pred, args_str = term.split('(', 1)
            args_str = args_str.rstrip(')')
            args = [a.strip() for a in args_str.split(',') if a.strip()]
            return pred.strip(), args
        return term, []
    
    def _evaluate_builtin(self, predicate: str, args: List[str]) -> bool:
        """Evaluate a builtin predicate"""
        if predicate in self.builtins:
            return self.builtins[predicate](*args)
        return False
    
    def _find_facts(self, pattern: str) -> List[Dict[str, str]]:
        """Find all facts matching a pattern, with variable bindings"""
        results = []
        for fact in self.facts:
            bindings = self._match(pattern, fact)
            if bindings is not None:
                results.append(bindings)
        return results
    
    def _solve_goal(self, goal: str, current_bindings: Dict[str, str], 
                   depth: int = 0, max_depth: int = 100) -> List[Dict[str, str]]:
        """
        Backward chaining: try to prove a goal.
        Returns list of successful variable bindings.
        """
        if depth > max_depth:
            return []
        
        # Check if this is a builtin predicate
        pred, args = self._parse_term(goal)
        if pred in self.builtins:
            # Evaluate with current bindings
            resolved_args = [self._resolve(arg, current_bindings) for arg in args]
            if self._evaluate_builtin(pred, resolved_args):
                return [current_bindings.copy()]
            return []
        
        results = []
        
        # First, try to match against facts
        pattern = self._apply_bindings(goal, current_bindings)
        fact_bindings = self._find_facts(pattern)
        
        for bindings in fact_bindings:
            # Merge bindings
            merged = current_bindings.copy()
            merged.update(bindings)
            results.append(merged)
        
        # Try to match against rule heads
        for head, body in self.rules:
            # We need to match the head against the goal, considering current bindings
            # The head might have variables that need to be bound
            head_bindings = self._match_with_bindings(head, goal, current_bindings)
            if head_bindings is not None:
                # Create new goal for each body atom
                new_bindings = current_bindings.copy()
                new_bindings.update(head_bindings)
                
                # Solve each body atom
                sub_results = [new_bindings.copy()]
                for body_atom in body:
                    new_sub_results = []
                    for binding in sub_results:
                        resolved_goal = self._apply_bindings(body_atom, binding)
                        sub_solutions = self._solve_goal(
                            resolved_goal, binding, depth + 1, max_depth
                        )
                        new_sub_results.extend(sub_solutions)
                    sub_results = new_sub_results
                    if not sub_results:
                        break
                
                results.extend(sub_results)
        
        return results
    
    def _resolve(self, term: str, bindings: Dict[str, str]) -> str:
        """Resolve variables in a term using current bindings"""
        if term[0].isupper() and term in bindings:
            return bindings[term]
        return term
    
    def _apply_bindings(self, goal: str, bindings: Dict[str, str]) -> str:
        """Apply bindings to a goal string"""
        pred, args = self._parse_term(goal)
        resolved_args = [self._resolve(arg, bindings) for arg in args]
        if resolved_args:
            return f"{pred}({', '.join(resolved_args)})"
        return pred
    
    def query(self, goal: str) -> List[Dict[str, str]]:
        """
        Query the knowledge base.
        Returns list of variable bindings that satisfy the goal.
        Handles conjunctions (commas) in goals.
        """
        goal = goal.strip().rstrip('.')
        
        # Check if this is a conjunction
        if ',' in goal:
            # Parse into multiple goals
            goals = self._parse_body(goal)
            if len(goals) > 1:
                # Solve as conjunction
                return self._solve_conjunction(goals, {}, max_depth=50)
        
        solutions = self._solve_goal(goal, {}, max_depth=50)
        return solutions
    
    def _solve_conjunction(self, goals: List[str], current_bindings: Dict[str, str], 
                           depth: int = 0, max_depth: int = 100) -> List[Dict[str, str]]:
        """Solve a conjunction of goals"""
        if depth > max_depth:
            return []
        
        if not goals:
            return [current_bindings.copy()]
        
        # Solve the first goal
        first_goal = goals[0]
        first_solutions = self._solve_goal(first_goal, current_bindings, depth, max_depth)
        
        if not first_solutions:
            return []
        
        # For each solution to the first goal, solve the rest
        results = []
        for binding in first_solutions:
            rest_solutions = self._solve_conjunction(goals[1:], binding, depth + 1, max_depth)
            results.extend(rest_solutions)
        
        return results
    
    def query_all(self, goal: str) -> List[Dict[str, str]]:
        """Find all solutions to a query"""
        return self.query(goal)

    def _extract_query_vars(self, query: str) -> Set[str]:
        """Extract variable names from a query string"""
        vars_found = set()
        for match in re.finditer(r'\b[A-Z][A-Za-z0-9_]*\b', query):
            vars_found.add(match.group())
        return vars_found

    def format_solutions(self, solutions: List[Dict[str, str]], query: str = None) -> str:
        """Format query solutions in a readable way, showing only query variables"""
        if not solutions:
            return "false."

        query_vars = self._extract_query_vars(query) if query else None

        results = []
        for sol in solutions:
            if sol:
                if query_vars is not None:
                    filtered = {k: v for k, v in sol.items() if k in query_vars}
                    if filtered:
                        bindings = ", ".join(f"{k} = {v}" for k, v in sorted(filtered.items()))
                        results.append(f"{{{bindings}}}")
                    else:
                        results.append("true")
                else:
                    bindings = ", ".join(f"{k} = {v}" for k, v in sorted(sol.items()))
                    results.append(f"{{{bindings}}}")
            else:
                results.append("true")

        return " ;\n".join(results) + "."


# ============================================================================
# DISCourse: LLM Interface Simulator
# ============================================================================

class LLMDiscourse:
    """
    Simulates an LLM as the 'Discourse' component.
    
    Responsibilities:
    - Interpret natural language queries
    - Formalize them into Prolog facts/rules
    - Reinterpret Prolog results back to natural language
    - Manage the neuro-symbolic loop
    """
    
    def __init__(self, prolog_engine: PrologEngine):
        self.prolog = prolog_engine
        self.domain_knowledge = {}
        self._init_domain_knowledge()
    
    def _init_domain_knowledge(self):
        """Initialize with some domain-specific templates"""
        # Classical logic
        self.domain_knowledge['classical_logic'] = {
            'interpreters': {
                r'(?i)\b(all|every)\s+(\w+)\s+are\s+(\w+)': 
                    lambda m: f"{m.group(1)}(X) :- {m.group(2)}(X).",
                r'(?i)\b(some|a|an)\s+(\w+)\s+are\s+(\w+)':
                    lambda m: f"{m.group(1)}(X) :- {m.group(2)}(X), {m.group(3)}(X).",
                r'(?i)(\w+)\s+is\s+a\s+(\w+)':
                    lambda m: f"{m.group(2)}({m.group(1)}).",
                r'(?i)(\w+)\s+is\s+(\w+)':
                    lambda m: f"{m.group(2)}({m.group(1)}).",
            },
            'reinterpreters': {
                'true': 'Yes, that is correct.',
                'false': 'No, that is not true based on the available knowledge.',
            }
        }
        
        # Family relationships
        self.domain_knowledge['family'] = {
            'interpreters': {
                r'(?i)(\w+)\s+is\s+the\s+(mother|father|parent)\s+of\s+(\w+)':
                    lambda m: f"parent({m.group(3)}, {m.group(1)}).",
                r'(?i)(\w+)\s+is\s+the\s+(son|daughter|child)\s+of\s+(\w+)':
                    lambda m: f"parent({m.group(3)}, {m.group(1)}).",
                r'(?i)(\w+)\s+and\s+(\w+)\s+are\s+siblings':
                    lambda m: f"parent(X, {m.group(1)}), parent(X, {m.group(2)}).",
            },
            'reinterpreters': {}
        }
        
        # Planning/Logistics
        self.domain_knowledge['planning'] = {
            'interpreters': {
                r'(?i)\b(create|define)\s+a\s+task\s+(\w+)\s+that\s+requires\s+(.+)':
                    lambda m: self._parse_requirements(m.group(2), m.group(1)),
                r'(?i)\b(task\s+(\w+)\s+requires\s+(.+))':
                    lambda m: self._parse_requirements(m.group(2), m.group(1)),
            },
            'reinterpreters': {}
        }
    
    def _parse_requirements(self, requirements: str, task: str) -> str:
        """Parse task requirements into Prolog rules"""
        # Simple version: just create a requires/2 fact
        return f"requires({task}, {requirements})."
    
    def interpret(self, text: str, domain: str = None) -> List[str]:
        """
        Interpret natural language text and generate Prolog representations.
        
        This simulates the LLM's ability to understand natural language
        and translate it into formal representations.
        """
        results = []
        
        # Determine domain if not specified
        if domain is None:
            domain = self._infer_domain(text)
        
        # Apply domain-specific patterns
        if domain in self.domain_knowledge:
            patterns = self.domain_knowledge[domain].get('interpreters', {})
            for pattern, handler in patterns.items():
                matches = re.findall(pattern, text)
                for match in matches:
                    try:
                        prolog_text = handler(match)
                        if prolog_text:
                            results.append(prolog_text)
                    except:
                        pass
        
        # General fallbacks
        if not results:
            results = self._general_interpretation(text)
        
        return results
    
    def _infer_domain(self, text: str) -> str:
        """Infer the most likely domain from the text"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['mother', 'father', 'parent', 'sibling', 'child']):
            return 'family'
        elif any(word in text_lower for word in ['task', 'require', 'plan', 'schedule']):
            return 'planning'
        elif any(word in text_lower for word in ['all', 'every', 'some', 'are', 'is a']):
            return 'classical_logic'
        else:
            return 'general'
    
    def _general_interpretation(self, text: str) -> List[str]:
        """General interpretation fallback"""
        results = []
        
        # Try to extract simple predicate-like statements
        # Pattern: X is a Y
        matches = re.findall(r'(\w+)\s+is\s+(?:a|an|the)\s+(\w+)', text, re.IGNORECASE)
        for subj, obj in matches:
            results.append(f"{obj}({subj}).")
        
        # Pattern: X are Y
        matches = re.findall(r'(\w+)\s+are\s+(\w+)', text, re.IGNORECASE)
        for subj, obj in matches:
            results.append(f"{obj}({subj}).")
        
        # Pattern: X has Y
        matches = re.findall(r'(\w+)\s+has\s+(\w+)', text, re.IGNORECASE)
        for subj, obj in matches:
            results.append(f"has({subj}, {obj}).")
        
        # Pattern: X Y Z (verb pattern)
        matches = re.findall(r'(\w+)\s+(\w+)\s+(\w+)', text)
        for subj, verb, obj in matches:
            results.append(f"{verb}({subj}, {obj}).")
        
        return results if results else [f"% Interpreted: {text}"]
    
    def formalize(self, text: str, domain: str = None) -> str:
        """
        Convert natural language to a complete Prolog program.
        
        This is the 'Formalize' step in the neuro-symbolic loop.
        """
        interpretations = self.interpret(text, domain)
        return "\n".join(interpretations)
    
    def derive(self, query_text: str, context: str = None) -> Tuple[str, List[Dict[str, str]]]:
        """
        Derive answers from the formal system.
        
        This combines:
        1. Formalizing the query (if needed)
        2. Running it through the Prolog engine (Geometry)
        3. Returning both the formal query and the results
        """
        # For now, assume query_text is already a Prolog query
        # In a real system, we'd formalize it first
        
        solutions = self.prolog.query(query_text)
        formal_query = query_text
        
        return formal_query, solutions
    
    def verify(self, statement: str) -> bool:
        """Verify if a statement is true in the formal system"""
        # Try to parse as a query
        solutions = self.prolog.query(statement)
        return len(solutions) > 0
    
    def reinterpret(self, solutions: List[Dict[str, str]], original_query: str = None) -> str:
        """
        Reinterpret formal results back into natural language.
        
        This is the 'Reinterpret' step in the neuro-symbolic loop.
        """
        if not solutions:
            return "No solutions found. The statement is false given the current knowledge."
        
        results = []
        for sol in solutions:
            if not sol:
                results.append("Yes, that is true.")
            else:
                bindings = ", ".join(f"{k} is {v}" for k, v in sol.items())
                results.append(f"Solution: {bindings}")
        
        return "\n".join(results)
    
    def loop(self, natural_language_query: str, domain: str = None, 
             max_iterations: int = 3) -> Dict:
        """
        Execute the complete neuro-symbolic loop:
        
        Interpret -> Formalize -> Derive -> Verify -> Reinterpret -> Revise
        
        Returns a dictionary with all intermediate results.
        """
        trace = {
            'natural_query': natural_language_query,
            'domain': domain or self._infer_domain(natural_language_query),
            'interpretations': [],
            'formal_query': None,
            'solutions': [],
            'verification': None,
            'reinterpretation': None,
            'iterations': []
        }
        
        for iteration in range(max_iterations):
            iteration_trace = {
                'iteration': iteration + 1,
                'input': natural_language_query if iteration == 0 else trace['reinterpretation']
            }
            
            # Step 1: Interpret (LLM)
            if iteration == 0:
                interpretations = self.interpret(natural_language_query, trace['domain'])
                trace['interpretations'] = interpretations
                iteration_trace['interpretations'] = interpretations
                
                # Step 2: Formalize (LLM) - load into Prolog
                for prog in interpretations:
                    self.prolog.load_program(prog)
                
                # For demo, we'll use a hardcoded query or extract one
                # In a real system, the LLM would generate this
                formal_query = self._extract_query(natural_language_query, trace['domain'])
                trace['formal_query'] = formal_query
                iteration_trace['formal_query'] = formal_query
                
                # Step 3: Derive (Prolog/Geometry)
                formal_query_for_engine, solutions = self.derive(formal_query)
                trace['solutions'] = solutions
                iteration_trace['solutions'] = solutions
                
                # Step 4: Verify (Prolog)
                verification = self.verify(formal_query)
                trace['verification'] = verification
                iteration_trace['verification'] = verification
                
                # Step 5: Reinterpret (LLM)
                reinterpretation = self.reinterpret(solutions, formal_query)
                trace['reinterpretation'] = reinterpretation
                iteration_trace['reinterpretation'] = reinterpretation
            
            trace['iterations'].append(iteration_trace)
            
            # Step 6: Revise - check if we need another iteration
            # For now, we'll stop after first iteration
            break
        
        return trace
    
    def _extract_query(self, text: str, domain: str) -> str:
        """Extract a Prolog query from natural language"""
        text_lower = text.lower()
        
        if domain == 'family':
            # "Who is the parent of Mary?" -> parent(X, mary)
            matches = re.findall(r'(?i)who\s+(is|are)\s+the\s+(\w+)\s+of\s+(\w+)', text)
            if matches:
                rel, _, obj = matches[0]
                return f"{rel}(X, {obj.lower()})."
            
            # "Is John the parent of Mary?" -> parent(john, mary)
            matches = re.findall(r'(?i)is\s+(\w+)\s+the\s+(\w+)\s+of\s+(\w+)', text)
            if matches:
                subj, rel, obj = matches[0]
                return f"{rel}({subj.lower()}, {obj.lower()})."
            
            # "Are X and Y siblings?" -> parent(Z, X), parent(Z, Y)
            matches = re.findall(r'(?i)are\s+(\w+)\s+and\s+(\w+)\s+siblings', text)
            if matches:
                a, b = matches[0]
                return f"parent(Z, {a.lower()}), parent(Z, {b.lower()})."
        
        elif domain == 'classical_logic':
            # "Is Socrates mortal?" -> mortal(socrates)
            matches = re.findall(r'(?i)is\s+(\w+)\s+(\w+)', text)
            if matches:
                subj, pred = matches[0]
                return f"{pred}({subj.lower()})."
            
            # "Who is mortal?" -> mortal(X)
            matches = re.findall(r'(?i)who\s+(is|are)\s+(\w+)', text)
            if matches:
                _, pred = matches[0]
                return f"{pred}(X)."
        
        # Default: try to find a predicate pattern
        words = text.split()
        if words:
            # Last word before ? might be what we're querying
            clean = re.sub(r'[?\.]', '', text).strip()
            # Simple heuristic: make first word lowercase, add (X) if it looks like a property
            first_word = words[0].lower()
            if first_word in ['who', 'what', 'which', 'is', 'are']:
                if len(words) > 1:
                    return f"{words[1].lower()}(X)."
            return f"{first_word}(X)."
        
        return "true."


# ============================================================================
# Neuro-Symbolic System: Combining Discourse and Geometry
# ============================================================================

class NeuroSymbolicSystem:
    """
    Complete neuro-symbolic AI system combining LLM (Discourse) and Prolog (Geometry).
    
    This demonstrates the thesis of the essay: that modern AI succeeds when it
    combines the linguistic breadth of LLMs with the formal constraint of
    symbolic systems.
    """
    
    def __init__(self):
        self.geometry = PrologEngine()
        self.discourse = LLMDiscourse(self.geometry)
    
    def run_loop(self, query: str, domain: str = None) -> Dict:
        """Run the complete neuro-symbolic loop"""
        return self.discourse.loop(query, domain)
    
    def demonstrate(self):
        """Run a series of demonstrations showing the neuro-symbolic approach"""
        print("=" * 80)
        print("NEURO-SYMBOLIC AI DEMONSTRATION")
        print("From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason")
        print("=" * 80)
        print()
        
        # Demo 1: Classical Logic (Aristotle)
        print("DEMO 1: CLASSICAL LOGIC (Aristotle's Syllogism)")
        print("-" * 80)
        self.demo_classical_logic()
        print()
        
        # Demo 2: Family Relationships (Ontology)
        print("DEMO 2: FAMILY RELATIONSHIPS (Platonic Ontology)")
        print("-" * 80)
        self.demo_family_relationships()
        print()
        
        # Demo 3: Expert System (Prolog's original use case)
        print("DEMO 3: EXPERT SYSTEM (Medical Diagnosis - like MYCIN)")
        print("-" * 80)
        self.demo_expert_system()
        print()
        
        # Demo 4: Planning (Constraint Reasoning)
        print("DEMO 4: PLANNING (Constraint-Based Reasoning)")
        print("-" * 80)
        self.demo_planning()
        print()
        
        # Demo 5: The Complete Loop
        print("DEMO 5: THE COMPLETE NEURO-SYMBOLIC LOOP")
        print("-" * 80)
        self.demo_complete_loop()
        print()
        
        print("=" * 80)
        print("CONCLUSION")
        print("=" * 80)
        print("These demonstrations show how Prolog (Geometry) provides the formal")
        print("reasoning structure that LLMs (Discourse) lack, while LLMs provide")
        print("the natural language interface that Prolog lacks.")
        print()
        print("Together, they realize the 2,500-year-old Platonic-Aristotelian vision")
        print("of intelligence as the manipulation of structured representations")
        print("according to structured rules.")
        print("=" * 80)
    
    def demo_classical_logic(self):
        """Demonstrate classical syllogistic reasoning"""
        print("\nScenario: Aristotle's classic syllogism")
        print('  Natural language: "All men are mortal. Socrates is a man. Is Socrates mortal?"')
        print()
        
        # Clear the knowledge base
        self.geometry.facts.clear()
        self.geometry.rules.clear()
        
        # Load the facts and rules (formalized by LLM)
        program = """
% Classical logic: Aristotle's syllogism
man(socrates).
man(plato).
man(aristotle).

mortal(X) :- man(X).
        """
        self.geometry.load_program(program)
        
        print("Formal representation (Geometry):")
        print("  man(socrates).")
        print("  man(plato).")
        print("  man(aristotle).")
        print("  mortal(X) :- man(X).")
        print()
        
        # Query
        print("Query: mortal(socrates).")
        solutions = self.geometry.query("mortal(socrates)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'mortal(socrates)')}")
        print()
        
        print("Reinterpretation (Discourse):")
        print("  Yes, Socrates is mortal.")
        print()
        
        # Show the power: ask a general question
        print("Query: mortal(X).")
        solutions = self.geometry.query("mortal(X)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'mortal(X)')}")
        print()
        print("Reinterpretation: All known men (Socrates, Plato, Aristotle) are mortal.")
    
    def demo_family_relationships(self):
        """Demonstrate ontology and relationship reasoning"""
        print("\nScenario: Family tree reasoning")
        print('  Natural language: "John is the father of Mary. Mary is the mother of Bob.')
        print('                     Who is the grandparent of Bob?"')
        print()
        
        # Clear the knowledge base
        self.geometry.facts.clear()
        self.geometry.rules.clear()
        
        # Load family facts
        program = """
% Family relationships
parent(john, mary).
parent(mary, bob).
parent(john, tom).
parent(susan, mary).

% Gender facts
male(john).
male(tom).
male(bob).
female(mary).
female(susan).

% Define parent relationships
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

% Grandparent relationship
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
        """
        self.geometry.load_program(program)
        
        print("Formal representation (Geometry):")
        print("  parent(john, mary).")
        print("  parent(mary, bob).")
        print("  father(X, Y) :- parent(X, Y), male(X).")
        print("  grandparent(X, Z) :- parent(X, Y), parent(Y, Z).")
        print()
        
        print("Query: grandparent(X, bob).")
        solutions = self.geometry.query("grandparent(X, bob)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'grandparent(X, bob)')}")
        print()
        print("Reinterpretation (Discourse):")
        print("  John and Susan are the grandparents of Bob.")
        print()
        
        print("Query: father(X, mary).")
        solutions = self.geometry.query("father(X, mary)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'father(X, mary)')}")
        print()
        print("Reinterpretation: John is the father of Mary.")
    
    def demo_expert_system(self):
        """Demonstrate expert system reasoning (like MYCIN)"""
        print("\nScenario: Medical diagnosis (simplified MYCIN-like system)")
        print('  Natural language: "The patient has fever and cough.')
        print('                     What could be the diagnosis?"')
        print()
        
        # Clear the knowledge base
        self.geometry.facts.clear()
        self.geometry.rules.clear()
        
        # Load medical knowledge
        program = """
% Medical expert system

% Symptoms
symptom(patient1, fever).
symptom(patient1, cough).
symptom(patient1, headache).
symptom(patient2, rash).
symptom(patient2, fever).

% Possible diagnoses
diagnosis(flu, X) :- symptom(X, fever), symptom(X, cough).
diagnosis(cold, X) :- symptom(X, cough), symptom(X, headache).
diagnosis(measles, X) :- symptom(X, rash), symptom(X, fever).

% Severity
severe(flu).
mild(cold).
mild(measles).
        """
        self.geometry.load_program(program)
        
        print("Formal representation (Geometry):")
        print("  symptom(patient1, fever).")
        print("  symptom(patient1, cough).")
        print("  diagnosis(flu, X) :- symptom(X, fever), symptom(X, cough).")
        print()
        
        print("Query: diagnosis(Disease, patient1).")
        solutions = self.geometry.query("diagnosis(Disease, patient1)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'diagnosis(Disease, patient1)')}")
        print()
        print("Reinterpretation (Discourse):")
        for sol in solutions:
            disease = sol.get('Disease', 'unknown')
            print(f"  Possible diagnosis: {disease.capitalize()}")
        print()

        # Show severity
        print("Query: diagnosis(D, patient1), severe(D).")
        solutions = self.geometry.query("diagnosis(D, patient1), severe(D)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'diagnosis(D, patient1), severe(D)')}")
        print()
        print("Reinterpretation: Flu is a severe diagnosis for patient1.")
    
    def demo_planning(self):
        """Demonstrate constraint-based planning"""
        print("\nScenario: Task scheduling with prerequisites")
        print('  Natural language: "We need to build a house.')
        print('                     Foundation must come before walls.')
        print('                     Walls must come before roof.')
        print('                     Roof must come before painting.')
        print('                     What tasks must come before painting?"')
        print()

        # Clear the knowledge base
        self.geometry.facts.clear()
        self.geometry.rules.clear()

        # Load planning knowledge
        program = """
% Task planning with prerequisites
task(foundation).
task(walls).
task(roof).
task(painting).

before(foundation, walls).
before(walls, roof).
before(roof, painting).

% Direct prerequisite
direct_prereq(A, B) :- before(A, B).

% Two-step prerequisite
two_step_prereq(A, C) :- before(A, B), before(B, C).

% Three-step prerequisite
three_step_prereq(A, D) :- before(A, B), before(B, C), before(C, D).
        """
        self.geometry.load_program(program)

        print("Formal representation (Geometry):")
        print("  task(foundation). task(walls). task(roof). task(painting).")
        print("  before(foundation, walls). before(walls, roof). before(roof, painting).")
        print("  direct_prereq(A, B) :- before(A, B).")
        print("  two_step_prereq(A, C) :- before(A, B), before(B, C).")
        print()

        print("Query: direct_prereq(X, painting).")
        solutions = self.geometry.query("direct_prereq(X, painting)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'direct_prereq(X, painting)')}")
        print()

        print("Query: two_step_prereq(X, painting).")
        solutions = self.geometry.query("two_step_prereq(X, painting)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'two_step_prereq(X, painting)')}")
        print()

        print("Query: three_step_prereq(X, painting).")
        solutions = self.geometry.query("three_step_prereq(X, painting)")
        print(f"Result: {self.geometry.format_solutions(solutions, 'three_step_prereq(X, painting)')}")
        print()

        print("Reinterpretation (Discourse):")
        print("  To paint, you must first complete: roof (direct),")
        print("  walls (2-step), and foundation (3-step).")
    
    def demo_complete_loop(self):
        """Demonstrate the complete neuro-symbolic loop"""
        print("\nScenario: Complete loop - from natural language to formal reasoning and back")
        print()
        
        # Start with a natural language question
        natural_query = "John is the father of Mary. Mary is the mother of Bob. Who is the grandfather of Bob?"
        
        print(f"Natural language query: {natural_query}")
        print()
        
        # Step 1: Interpret and Formalize
        print("Step 1-2: INTERPRET & FORMALIZE (Discourse -> Geometry)")
        self.geometry.facts.clear()
        self.geometry.rules.clear()
        
        # Simulate LLM interpretation
        print("  LLM interprets the relationships and generates:")
        formal_facts = [
            "parent(john, mary).",
            "parent(mary, bob).",
            "male(john).",
            "female(mary)."
        ]
        for fact in formal_facts:
            print(f"    {fact}")
            self.geometry.add_fact(fact)
        
        # LLM also generates the grandfather rule
        formal_rule = "grandfather(X, Z) :- parent(X, Y), parent(Y, Z), male(X)."
        print(f"    {formal_rule}")
        self.geometry.add_rule(formal_rule)
        print()
        
        # Step 3: Derive
        print("Step 3: DERIVE (Geometry)")
        query = "grandfather(X, bob)"
        print(f"  Query: {query}")
        solutions = self.geometry.query(query)
        print(f"  Formal result: {self.geometry.format_solutions(solutions, query)}")
        print()
        
        # Step 4: Verify
        print("Step 4: VERIFY (Geometry)")
        is_verified = self.geometry.query("grandfather(john, bob)")
        print(f"  Verify grandfather(john, bob): {self.geometry.format_solutions(is_verified)}")
        print()
        
        # Step 5: Reinterpret
        print("Step 5: REINTERPRET (Discourse)")
        if solutions:
            binding = solutions[0]
            grandfather = binding.get('X', 'unknown')
            print(f"  Natural language answer: {grandfather.capitalize()} is the grandfather of Bob.")
        else:
            print("  Natural language answer: No grandfather found for Bob.")
        print()
        
        # Step 6: Revise (if needed)
        print("Step 6: REVISE (Loop)")
        print("  If the answer is unsatisfactory, the LLM can refine the formalization")
        print("  and the loop continues. In this case, the answer is correct,")
        print("  so we stop here.")


# ============================================================================
# Interactive Mode
# ============================================================================

def interactive_mode():
    """Run in interactive mode"""
    system = NeuroSymbolicSystem()
    
    print("Interactive Neuro-Symbolic System")
    print("Type 'help' for commands, 'quit' to exit, 'demo' to run demonstrations")
    print()
    
    while True:
        try:
            cmd = input("ns> ").strip()
            
            if not cmd:
                continue
            
            if cmd.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            elif cmd.lower() in ['help', 'h', '?']:
                print("\nCommands:")
                print("  help, h, ?      - Show this help")
                print("  quit, exit, q   - Quit the system")
                print("  demo            - Run all demonstrations")
                print("  clear           - Clear the knowledge base")
                print("  load <file>     - Load a Prolog program from file")
                print("  assert <fact>   - Add a fact to the knowledge base")
                print("  rule <rule>     - Add a rule to the knowledge base")
                print("  query <goal>    - Query the knowledge base")
                print("  natural <text>  - Process natural language query")
                print()
            
            elif cmd.lower() in ['demo', 'demos']:
                system.demonstrate()
            
            elif cmd.lower() in ['clear', 'reset']:
                system.geometry.facts.clear()
                system.geometry.rules.clear()
                print("Knowledge base cleared.")
            
            elif cmd.lower().startswith('load '):
                filename = cmd[5:].strip()
                try:
                    with open(filename, 'r') as f:
                        program = f.read()
                    system.geometry.load_program(program)
                    print(f"Loaded {filename}")
                except FileNotFoundError:
                    print(f"File not found: {filename}")
                except Exception as e:
                    print(f"Error: {e}")
            
            elif cmd.lower().startswith('assert '):
                fact = cmd[7:].strip().rstrip('.')
                system.geometry.add_fact(fact)
                print(f"Added fact: {fact}")
            
            elif cmd.lower().startswith('rule '):
                rule = cmd[5:].strip().rstrip('.')
                system.geometry.add_rule(rule)
                print(f"Added rule: {rule}")
            
            elif cmd.lower().startswith('query '):
                query = cmd[6:].strip().rstrip('.')
                solutions = system.geometry.query(query)
                print(system.geometry.format_solutions(solutions))
            
            elif cmd.lower().startswith('natural '):
                text = cmd[8:].strip()
                trace = system.run_loop(text)
                print("\nTrace:")
                print(f"  Domain: {trace['domain']}")
                print(f"  Interpretations: {trace['interpretations']}")
                print(f"  Formal query: {trace['formal_query']}")
                print(f"  Solutions: {trace['solutions']}")
                print(f"  Verification: {trace['verification']}")
                print(f"  Reinterpretation: {trace['reinterpretation']}")
            
            else:
                # Try as a query
                solutions = system.geometry.query(cmd)
                print(system.geometry.format_solutions(solutions))
        
        except KeyboardInterrupt:
            print("\nUse 'quit' to exit")
        except EOFError:
            print()
            break
        except Exception as e:
            print(f"Error: {e}")


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    import sys
    
    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--demo', '-d']:
            system = NeuroSymbolicSystem()
            system.demonstrate()
        elif sys.argv[1] in ['--interactive', '-i']:
            interactive_mode()
        elif sys.argv[1] in ['--help', '-h']:
            print("Usage: python neuro_symbolic_demo.py [--demo | --interactive | --help]")
            print("  --demo, -d      Run demonstrations")
            print("  --interactive, -i  Run in interactive mode")
            print("  --help, -h      Show this help")
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help for usage information")
    else:
        # Default: run demonstrations
        system = NeuroSymbolicSystem()
        system.demonstrate()
