import gradio as gr
import random

def monte_carlo_failure_probability(num_simulations, failure_threshold):
    failures = 0
    for _ in range(num_simulations):
        result = random.random()
        if result < failure_threshold:
            failures += 1
    return failures / num_simulations

def main():
    num_simulations = 10000
    failure_threshold = 0.05
    probability = monte_carlo_failure_probability(num_simulations, failure_threshold)
    print(f"Probability of failure: {probability}")

if __name__ == "__main__":
    main()
    
    def gradio_interface(num_simulations, failure_threshold):
        probability = monte_carlo_failure_probability(num_simulations, failure_threshold)
        return f"Probability of failure: {probability}"

    iface = gr.Interface(
        fn=gradio_interface,
        inputs=[
            gr.Number(value=10000, label="Number of Simulations"),
            gr.Number(value=0.05, label="Failure Threshold")
        ],
        outputs="text",
        title="Monte Carlo Failure Probability",
        description="Calculate the probability of failure using Monte Carlo simulation."
    )

    iface.launch()