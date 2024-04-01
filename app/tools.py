from langchain.tools import tool


@tool
def roe(
    net_income: float,
    equity: float,
) -> float:
    """
    Computes the return on equity (ROE) for a given company.
    Use this function to evaluate the profitability of a company.
    """
    return net_income / equity


@tool
def roic(
    operating_income: float,
    total_debt: float,
    equity: float,
    cash_and_equivalents: float,
    tax_rate: float = 0.35,
) -> float:
    """
    Computes the return on invested capital (ROIC) for a given company.
    Use this function to evaluate the efficiency of a company in generating returns from its capital.
    """
    net_operating_profit_after_tax = operating_income * (1 - tax_rate)
    invested_capital = total_debt + equity - cash_and_equivalents
    return net_operating_profit_after_tax / invested_capital


@tool
def owner_earnings(
    net_income: float,
    depreciation_amortization: float = 0.0,
    capital_expenditures: float = 0.0
):
    """
    Calculates the owner earnings for a company based on the net income, depreciation/amortization, and capital expenditures.
    """
    return net_income + depreciation_amortization - capital_expenditures


@tool
def discounted_cash_flow(
    free_cash_flow: float,
    growth_rate: float = 0.05,
    discount_rate: float = 0.10,
    terminal_growth_rate: float = 0.02,
    num_years: int = 5,
) -> float:
    """
    Computes the discounted cash flow (DCF) for a given company based on the current free cash flow.
    Use this function to calculate the intrinsic value of a stock.
    """
    # Estimate the future cash flows based on the growth rate
    cash_flows = [free_cash_flow * (1 + growth_rate) ** i for i in range(num_years)]

    # Calculate the present value of projected cash flows
    present_values = []
    for i in range(num_years):
        present_value = cash_flows[i] / (1 + discount_rate) ** (i + 1)
        present_values.append(present_value)

    # Calculate the terminal value
    terminal_value = cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    terminal_present_value = terminal_value / (1 + discount_rate) ** num_years

    # Sum up the present values and terminal value
    dcf_value = sum(present_values) + terminal_present_value

    return dcf_value
