from rapidfuzz import fuzz, process

# 1. THE DATA (Your 'offline' downloaded list)
sanctions_list = ["Vladimir Putin", "Slobodan Milosevic", "Osama Bin Laden", "John Doe"]

def screen_name(input_name):
    print(f"\n--- Screening: {input_name} ---")
    
    # We compare the input against every name in our list
    for entry in sanctions_list:
        # Calculate the 'Token Sort Ratio' (handles name shuffling like 'Doe, John')
        score = fuzz.token_sort_ratio(input_name, entry)
        
        # 2. SCORE BANDS (The 'Logic')
        if score >= 95:
            decision = "🚨 RED ALERT: EXACT MATCH"
            rationale = "High confidence; potential evasion attempt or exact hit."
        elif 80 <= score < 95:
            decision = "⚠️ AMBER: MANUAL REVIEW"
            rationale = f"Similarity score of {score}. Possible typo or alias."
        elif 65 <= score < 80:
            decision = "🔍 GREEN: LOW PROBABILITY"
            rationale = "Weak phonetic similarity; monitor only."
        else:
            continue # Ignore noise below 65%

        print(f"Match: {entry} | Score: {score}")
        print(f"Status: {decision}")
        print(f"Rationale: {rationale}")

# Test Cases
screen_name("John Doe")          # Exact Match (100)
screen_name("Jon Doe")           # High Score (93) - Typo detection
screen_name("Doe John")          # High Score (100) - Order change
screen_name("Jane Doe")          # Low Score (75) - Different first name