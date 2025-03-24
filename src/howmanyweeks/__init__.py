def main() -> None:
    from datetime import datetime, timedelta
    import argparse

    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Please use YYYY-MM-DD.")

    # Default start and end dates
    default_start_date = datetime(2020, 8, 10)
    default_end_date = datetime.now()

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Calculate the number of weeks or days between two dates.")
    parser.add_argument('--start_date', type=parse_date, default=default_start_date, help="Start date in YYYY-MM-DD format (default: 2020-08-10)")
    parser.add_argument('--end_date', type=parse_date, default=default_end_date, help="End date in YYYY-MM-DD format (default: current date)")
    parser.add_argument('--unit', '-u', choices=['weeks', 'days'], default='weeks', help="Unit of time to calculate difference (default: weeks)")

    args = parser.parse_args()

    start_date = args.start_date
    end_date = args.end_date
    unit = args.unit

    if unit == 'weeks':
        weeks = []
        current_date = start_date
        while current_date <= end_date:
            weeks.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(weeks=1)
        print(len(weeks))
    elif unit == 'days':
        delta = end_date - start_date
        print(delta.days+1)
