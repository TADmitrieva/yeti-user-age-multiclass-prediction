
def create_feature_space(df_u, df_ads, df_surf, df_dev, df_cloud):
    feature_space = df_u.copy()
    feature_space = feature_space.merge(df_ads, on='user_id', how='left')
    feature_space = feature_space.merge(df_surf, on='user_id', how='left')
    feature_space = feature_space.merge(df_dev, on='user_id', how='left')
    feature_space = feature_space.merge(df_cloud, on='user_id', how='left')
    feature_space = feature_space.set_index('user_id')
    return feature_space
