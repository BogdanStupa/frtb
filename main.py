from frtb.range_frtb_bucket import RangeFrtbBucket
from frtb.value_frtb_bucket import ValueFrtbBucket


if __name__ == '__main__':

    value_bucket = ValueFrtbBucket("frtb-value.csv")
    frtb_values = ["Finance", "Finance1", "Agriculture", "Agriculture1", "Technologies", "Technologies1", "ef"]

    for frtb_value in frtb_values:
        print(value_bucket.get_bucket(frtb_value))

    print()
    range_bucket = RangeFrtbBucket("frtb-range.csv")
    frtb_range_values = [1, 2, 5, 7, 3, 9, 10, 15, 22, 33, 55]

    for frtb_range_value in frtb_range_values:
        print(range_bucket.get_bucket(frtb_range_value))


