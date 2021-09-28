from frtb import ValueFrtbBucket, RangeFrtbBucket

if __name__ == '__main__':

    value_bucket = ValueFrtbBucket("frtb-value.csv")
    frtb_values = [["Finance", 1], ["Finance1", 4], ["Agriculture", 2], ["Agriculture1", 5],
                   ["Technologies", 3], ["Technologies1", 6], ["ef", -1]]

    for frtb_value in frtb_values:
        assert value_bucket.get_bucket(frtb_value[0]) == frtb_value[1], f"for [{frtb_value[0]}] invalid bucket"


    range_bucket = RangeFrtbBucket("frtb-range.csv")
    frtb_ranges = [[0 ,1], [1, 1], [5,1], [9, 1], [10, 2], [15, 2], [22, -1],
                         [33, 4], [55, 3], [68, 3], [70, 5], [100, 5], [40, 6]]

    for frtb_range in frtb_ranges:
        assert range_bucket.get_bucket(frtb_range[0]) == frtb_range[1], f"for [{frtb_range[0]}] invalid bucket"

