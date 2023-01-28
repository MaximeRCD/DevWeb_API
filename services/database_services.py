from database import scans,database
async def save_prediction(predicition):
    query = scans.insert().values(
        user_id=predicition.user_id,
        predicted_class=predicition.predicted_class,
        score=predicition.score
    )
    try:
        insertion = await database.execute(query)
        return {"Result added"}

    except Exception as e:
        print(e)
        return {e}