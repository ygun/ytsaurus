DEPENDS(
    mapreduce/yt/tests/native/remote_copy/recipe
    yt/packages/latest
    contrib/tools/python
)

USE_RECIPE(
    mapreduce/yt/tests/native/remote_copy/recipe/two_cluster_recipe
)