import matplotlib.pyplot as plt

def generate_bar_graph():
    # Sample data
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
    values = [10, 24, 17, 12]
    
    # Create a bar plot
    plt.bar(categories, values)
    
    # Set the title and labels
    plt.title('Bar Graph')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    
    # Display the plot
    plt.show()

# Call the function to generate the bar graph
generate_bar_graph()
