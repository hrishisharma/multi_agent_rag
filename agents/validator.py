def validate_answer(answer, context):
    overlap_count = 0

    answer_words = answer.lower().split()
    context_words = context.lower().split()

    for word in answer_words:
        if word in context_words:
            overlap_count += 1

    if overlap_count > 20:
        return "Answer strongly grounded in retrieved context.", "High"

    elif overlap_count > 10:
        return "Answer partially grounded in retrieved context.", "Medium"

    return "Answer may contain unsupported information.", "Low"