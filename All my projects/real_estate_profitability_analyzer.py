# ============================================
# REAL ESTATE PROFITABILITY ANALYZER
# ============================================

# ITP = Property Transfer Tax (Impuesto de Transmisiones Patrimoniales)
itp_rates = {
    "Madrid": 6.0,
    "Catalonia": 10.0,
    "Andalusia": 8.0,
    "Valencia": 10.0,
    "Basque Country": 4.0,
    "Galicia": 10.0,
    "Castile and León": 8.0,
    "Castile-La Mancha": 9.0,
    "Murcia": 8.0,
    "Aragon": 8.0,
    "Canary Islands": 6.5,
    "Extremadura": 8.0,
    "Asturias": 8.0,
    "Balearic Islands": 8.0,
    "Cantabria": 10.0,
    "La Rioja": 7.0,
    "Navarre": 6.0,
    "Ceuta": 6.0,
    "Melilla": 6.0
}

def create_property(address, price, sqm, bedrooms, autonomous_region, property_type):
    """
    Creates a dictionary with all the property information.

    Returns:
    dict: Dictionary with the property's full information
    """
    property_data = {
        "address": address,
        "purchase_price": price,
        "square_meters": sqm,
        "bedrooms": bedrooms,
        "autonomous_region": autonomous_region,
        "property_type": property_type,
        "price_per_sqm": price / sqm
    }
    return property_data


def create_financing(down_payment_percentage, annual_rate, term_years, total_price):
    """
    Creates a dictionary with the financing information.

    Returns:
    dict: Dictionary with the financing data
    """
    down_payment_amount = total_price * (down_payment_percentage / 100)
    financed_amount = total_price - down_payment_amount

    # Calculate monthly payment (amortization formula)
    monthly_rate = (annual_rate / 100) / 12
    num_payments = term_years * 12
    monthly_payment = financed_amount * (monthly_rate * ((1 + monthly_rate) ** num_payments)) / (((1 + monthly_rate) ** num_payments) - 1)

    financing = {
        "down_payment_percentage": down_payment_percentage,
        "down_payment_amount": down_payment_amount,
        "financed_amount": financed_amount,
        "annual_rate": annual_rate,
        "term_years": term_years,
        "monthly_payment": monthly_payment,
        "total_to_pay": monthly_payment * num_payments
    }
    return financing


def calculate_property_tax(purchase_price, property_type):
    """
    Automatically calculates the annual property tax (IBI) based on the property type.

    Parameters:
    purchase_price (float): Purchase price of the property
    property_type (str): "Urban" or "Rural"

    Returns:
    float: Annual property tax (IBI)
    """
    # Cadastral value is approximately 70% of the purchase price
    cadastral_value = purchase_price * 0.70

    # Apply rate based on type
    tax_rate = 0.00428 * (property_type == "Urban") + 0.00567 * (property_type == "Rural")
    annual_property_tax = cadastral_value * tax_rate

    return annual_property_tax


def calculate_list_total(expense_list):
    """
    Sums all the expenses in a list of tuples.

    Parameters:
    expense_list (list): List of tuples (concept, amount)

    Returns:
    float: Sum total
    """
    total = 0
    total += expense_list[0][1]  # First monthly expense
    total += expense_list[1][1]  # Second monthly expense
    total += expense_list[2][1]  # Third monthly expense
    return total


def create_rental_income(monthly_rent, months_occupied):
    """
    Creates a dictionary with rental income information.

    Returns:
    dict: Dictionary with income data
    """
    income = {
        "monthly_rent": monthly_rent,
        "months_occupied": months_occupied,
        "annual_income": monthly_rent * months_occupied,
        "occupancy_rate": (months_occupied / 12) * 100
    }
    return income


def calculate_initial_purchase_costs(price, autonomous_region):
    """
    Calculates the initial purchase costs based on the autonomous region.
    Returns a tuple with the breakdown.

    Returns:
    tuple: (transfer_tax, notary_and_registry, total)
    """
    # Get the ITP rate for the region
    itp_rate = itp_rates[autonomous_region]

    # Calculate costs
    transfer_tax = price * (itp_rate / 100)
    notary_and_registry = price * 0.015  # Approximate notary and registry cost
    total = transfer_tax + notary_and_registry

    return (transfer_tax, notary_and_registry, total)


def calculate_profitability_metrics(annual_income, annual_operating_expenses, total_annual_expenses, property_price, initial_investment):
    """
    Calculates multiple metrics and returns a tuple.

    Returns:
    tuple: (gross_yield, net_yield, cap_rate, payback_years)
    """
    # Gross yield: annual income / purchase price
    gross_yield = (annual_income / property_price) * 100

    # Net profit after all annual expenses
    net_profit = annual_income - total_annual_expenses

    # Net yield: net profit / initial investment
    net_yield = (net_profit / initial_investment) * 100

    # Approximate CAP (Capitalization) Rate
    # Operating expenses are: community fees + insurance + maintenance + property tax + extra maintenance
    noi = annual_income - annual_operating_expenses
    cap_rate = (noi / property_price) * 100

    # ROI expressed as years to recover the investment (payback period)
    payback_years = initial_investment / net_profit

    return (gross_yield, net_yield, cap_rate, payback_years)


def calculate_cash_flow(income_dict, monthly_expenses_list, mortgage_payment):
    """
    Calculates the monthly cash flow.

    Returns:
    tuple: (monthly_cash_flow, annual_cash_flow)
    """
    rent = income_dict["monthly_rent"]
    monthly_expenses = calculate_list_total(monthly_expenses_list)

    monthly_cash_flow = rent - mortgage_payment - monthly_expenses
    annual_cash_flow = monthly_cash_flow * 12

    return (monthly_cash_flow, annual_cash_flow)


def evaluate_investment(net_yield, cap_rate, monthly_cash_flow):
    """
    Evaluates the investment and returns a tuple with score and recommendation.

    Returns:
    tuple: (score, recommendation, traffic_light)
    """
    score = 0
    score += 40 * (net_yield >= 6)
    score += 30 * (cap_rate >= 5)
    score += 30 * (monthly_cash_flow > 0)

    # Recommendation based on score
    recommendation = "EXCELLENT INVESTMENT" * (score >= 80) + \
                      "GOOD INVESTMENT" * (60 <= score < 80) + \
                      "MODERATE INVESTMENT" * (40 <= score < 60) + \
                      "RISKY INVESTMENT" * (score < 40)

    traffic_light = "🟢" * (score >= 70) + "🟡" * (40 <= score < 70) + "🔴" * (score < 40)

    return (score, recommendation, traffic_light)


def request_property_data():
    """
    Asks the user for the property data and returns a dictionary.

    Returns:
    dict: Dictionary with the full information
    """
    print("\n" + "="*60)
    print("🏠 PROPERTY DATA")
    print("="*60)

    address = input("\n📍 Address: ")
    price = float(input("💰 Purchase price (€): "))
    sqm = float(input("📏 Square meters: "))
    bedrooms = int(input("🛏️  Number of bedrooms: "))
    property_type = input("🏘️  Property type (Urban/Rural): ")

    # Show available autonomous regions
    print("\n🗺️  AUTONOMOUS REGIONS:")
    regions_list = list(itp_rates)

    print(f"   {regions_list[0]}, {regions_list[1]}, {regions_list[2]}")
    print(f"   {regions_list[3]}, {regions_list[4]}, {regions_list[5]}")
    print(f"   {regions_list[6]}, {regions_list[7]}, {regions_list[8]}")
    print(f"   (and more...)")

    region = input("\n🏛️  Autonomous region: ")

    property_data = create_property(address, price, sqm, bedrooms, region, property_type)

    print("\n" + "="*60)
    print("💳 FINANCING")
    print("="*60)

    down_payment_pct = float(input("\n💵 Down payment percentage (%): "))
    rate = float(input("📈 Annual interest rate (%): "))
    term = int(input("📅 Term in years: "))

    financing = create_financing(down_payment_pct, rate, term, price)

    print("\n" + "="*60)
    print("🏦 EXPECTED INCOME")
    print("="*60)

    rent = float(input("\n💸 Estimated monthly rent (€): "))
    months_occ = int(input("📆 Months occupied per year (10-12): "))

    income = create_rental_income(rent, months_occ)

    print("\n" + "="*60)
    print("💸 MONTHLY EXPENSES")
    print("="*60)

    community_fee = float(input("\n🏢 Community fees (€): "))
    insurance = float(input("🛡️  Insurance (monthly) (€): "))
    maintenance = float(input("🔧 Maintenance (monthly) (€): "))

    monthly_expenses = [
        ("Community fees", community_fee),
        ("Insurance", insurance),
        ("Maintenance", maintenance)
    ]

    print("\n" + "="*60)
    print("💸 EXTRA ANNUAL EXPENSES")
    print("="*60)

    # Calculate property tax (IBI) automatically
    property_tax = calculate_property_tax(price, property_type)
    print(f"\n🏛️  Automatically calculated property tax (IBI): {property_tax:,.2f}€")

    extra_maintenance = float(input("🔨 Extraordinary maintenance (annual) (€): "))

    annual_expenses = [
        ("Property tax (IBI)", property_tax),
        ("Extraordinary maintenance", extra_maintenance)
    ]

    # Create the complete dictionary with all the data
    full_analysis = {
        "property": property_data,
        "financing": financing,
        "income": income,
        "monthly_expenses": monthly_expenses,
        "annual_expenses": annual_expenses,
        "expense_categories": {"Mortgage", "Maintenance", "Taxes", "Insurance", "Community fees"},  # Set of expense categories
        "available_regions": itp_rates
    }

    return full_analysis


def show_full_report(data):
    """
    Generates the full report using the data dictionary.

    Parameters:
    data (dict): Dictionary with all the analysis information
    """
    # Extract data from the nested dictionaries
    property_data = data["property"]
    financing = data["financing"]
    income = data["income"]
    monthly_expenses = data["monthly_expenses"]
    annual_expenses = data["annual_expenses"]

    print("\n\n" + "="*70)
    print("📊 REAL ESTATE PROFITABILITY ANALYSIS")
    print("="*70)

    # BASIC INFORMATION
    print(f"\n🏠 PROPERTY")
    print(f"   📍 Address: {property_data['address']}")
    print(f"   💰 Price: {property_data['purchase_price']:,.0f}€")
    print(f"   📏 Surface area: {property_data['square_meters']}m²")
    print(f"   🛏️  Bedrooms: {property_data['bedrooms']}")
    print(f"   🏘️  Type: {property_data['property_type']}")
    print(f"   🏛️  Region: {property_data['autonomous_region']}")
    print(f"   📐 Price/m²: {property_data['price_per_sqm']:,.2f}€")

    # FINANCING
    print(f"\n💳 FINANCING")
    print(f"   Down payment ({financing['down_payment_percentage']}%): {financing['down_payment_amount']:,.0f}€")
    print(f"   Financed amount: {financing['financed_amount']:,.0f}€")
    print(f"   Rate: {financing['annual_rate']}% annual")
    print(f"   Term: {financing['term_years']} years")
    print(f"   Monthly payment: {financing['monthly_payment']:,.2f}€")
    print(f"   Total to pay: {financing['total_to_pay']:,.0f}€")

    # PURCHASE COSTS
    transfer_tax, notary_and_registry, total_purchase_cost = calculate_initial_purchase_costs(
        property_data['purchase_price'],
        property_data['autonomous_region']
    )
    itp_rate = data["available_regions"][property_data['autonomous_region']]
    print(f"\n📋 INITIAL COSTS")
    print(f"   Transfer tax - ITP ({itp_rate}%): {transfer_tax:,.0f}€")
    print(f"   Notary and registry: {notary_and_registry:,.0f}€")
    print(f"   Total purchase costs: {total_purchase_cost:,.0f}€")

    initial_investment = financing['down_payment_amount'] + total_purchase_cost
    print(f"\n💵 TOTAL INITIAL INVESTMENT: {initial_investment:,.0f}€")

    # INCOME
    print(f"\n📈 PROJECTED INCOME")
    print(f"   Monthly rent: {income['monthly_rent']:,.0f}€")
    print(f"   Months occupied: {income['months_occupied']}/12")
    print(f"   Occupancy rate: {income['occupancy_rate']:.1f}%")
    print(f"   Annual income: {income['annual_income']:,.0f}€")

    # MONTHLY EXPENSES
    print(f"\n💸 MONTHLY EXPENSES")
    print(f"   {monthly_expenses[0][0]}: {monthly_expenses[0][1]:,.0f}€")
    print(f"   {monthly_expenses[1][0]}: {monthly_expenses[1][1]:,.0f}€")
    print(f"   {monthly_expenses[2][0]}: {monthly_expenses[2][1]:,.0f}€")
    total_monthly_expenses = calculate_list_total(monthly_expenses)
    print(f"   Monthly subtotal: {total_monthly_expenses:,.0f}€")

    # ANNUAL EXPENSES
    print(f"\n💸 EXTRA ANNUAL EXPENSES")
    print(f"   {annual_expenses[0][0]}: {annual_expenses[0][1]:,.0f}€")
    print(f"   {annual_expenses[1][0]}: {annual_expenses[1][1]:,.0f}€")
    extra_annual_expenses = annual_expenses[0][1] + annual_expenses[1][1]

    total_annual_expenses = (total_monthly_expenses * 12) + extra_annual_expenses + (financing['monthly_payment'] * 12)
    total_annual_operating_expenses = (total_monthly_expenses * 12) + extra_annual_expenses  # without mortgage
    print(f"   Total annual expenses (with mortgage): {total_annual_expenses:,.0f}€")

    # CATEGORIES
    print(f"\n🏷️  EXPENSE CATEGORIES")
    categories_list = sorted(data["expense_categories"])
    print(f"   {', '.join(categories_list)}")

    # CASH FLOW
    monthly_cf, annual_cf = calculate_cash_flow(
        income,
        monthly_expenses,
        financing['monthly_payment']
    )
    print(f"\n💰 CASH FLOW")
    print(f"   Monthly: {monthly_cf:,.2f}€")
    print(f"   Annual: {annual_cf:,.2f}€")

    # PROFITABILITY
    gross_yield, net_yield, cap_rate, payback_years = calculate_profitability_metrics(
        income['annual_income'],
        total_annual_operating_expenses,
        total_annual_expenses,
        property_data['purchase_price'],
        initial_investment
    )

    print(f"\n📊 PROFITABILITY INDICATORS")
    print(f"   Gross yield: {gross_yield:.2f}%")
    print(f"   Net yield: {net_yield:.2f}%")
    print(f"   CAP Rate: {cap_rate:.2f}%")
    print(f"   Payback period: {abs(payback_years):.1f} years")

    # EVALUATION
    score, recommendation, traffic_light = evaluate_investment(net_yield, cap_rate, monthly_cf)

    print(f"\n🎯 FINAL EVALUATION")
    print(f"   Score: {score}/100")
    print(f"   {traffic_light} {recommendation}")

    print("\n" + "="*70)



# ============================================
# MAIN PROGRAM
# ============================================

header = """
╔══════════════════════════════════════════════════════════════════╗
║             🏢 REAL ESTATE INVESTMENT ANALYZER 🏢                ║
║                                                                  ║
║               Rental profitability analysis                     ║
║                          Spain                                   ║
╚══════════════════════════════════════════════════════════════════╝
"""
print(header)

print("\n💡 Welcome to the real estate investment analyzer")
print("    This system will help you evaluate whether buying a home")
print("    to rent it out is a good investment.\n")

# Request data from the user
full_data = request_property_data()

# Generate report
show_full_report(full_data)

# Final notes
print("\n💡 IMPORTANT NOTES:")
print("   • This analysis uses general estimates")
print("   • Net yield >6% = Excellent | 4-6% = Good | <4% = Low")
print("   • CAP Rate >5% = Recommended for stable markets")
print("\n✨ Thank you for using the Analyzer! ✨\n")