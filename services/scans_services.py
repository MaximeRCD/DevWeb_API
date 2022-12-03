from database import database, scans
import pandas as pd


SCAN_CLASSES = ["GlassOrMetal", "Other", "Organic", "Plastic", "Paper"]


def get_all_scans():
    query = scans.select()
    return database.fetch_all(query)


def get_scans_by_user_id(user_id: int):
    query = scans.select().where(scans.c.user_id == user_id)
    return database.fetch_all(query)


async def get_pcs_scans_stats(user_id: int = None):
    if user_id:
        all_scans = await get_scans_by_user_id(user_id)
    else:
        all_scans = await get_all_scans()
    all_scans_df = pd.DataFrame(all_scans, columns=["user_id","predicted_class","date","score"])
    classes_cardinality = all_scans_df.groupby(["predicted_class"]).size().to_dict()
    return classes_cardinality


