'''
file of EDA and graphing
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

def hist_perc_new(col):
    plt.hist(col, bins = 60, color = '#F1D78C')
    plt.title("Each Users Average Percentage of NEW Items")
    plt.xlabel('Percentage of NEW Items')
    plt.ylabel('Number of Users')
    plt.show();

def hist_avg_cart(col):
    plt.hist(col, bins = 100, color = '#F46708')
    plt.title("Each Users Average Cart Order")
    plt.xlabel('Average Cart Order')
    plt.ylabel('Number of Users')
    plt.show();

def score_f1(model, f1, mean_acc):
    # #---    Graph Score and F1 and Model
    fonttitle = {'fontname':'Helvetica', 'fontsize':30}
    fig, ax = plt.subplots(figsize = (20, 10))
    ax.plot(model, f1, color= '#EF727F', marker='*', linewidth = 5, label = 'F1 Score')
    ax.plot(model, mean_acc, color='#F6A811', marker='*', linewidth = 5, label = 'Mean Accuracy Score')     
    ax.set_ylim(ymin = 0.1, ymax = 0.9)
    ax.tick_params(axis='both', which='major', labelsize=18)
    plt.legend()
    plt.xticks(rotation = 10)
    plt.title('Do you order something Organic? \n Mean Accuracy Score and F1 Score by Model', fontdict=fonttitle)
    plt.show();

def make_bar(df, col_x, col_y, title, x_label, y_label):
    fonttitle = {'fontname':'Helvetica', 'fontsize':30}
    fig, ax = plt.subplots(figsize = (20, 10))
    ax = sns.barplot(df[col_x], df[col_y], palette = citrus)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    # ax.tick_params(axis='both', which='major', labelsize=18)
    plt.title(title, fontdict=fonttitle)
    plt.show();

def get_one_item():
    order_train = pd.read_csv('../../instacart_data/order_products__train.csv')
    order_prior = pd.read_csv("../../instacart_data/order_products__prior.csv")
    products = pd.read_csv("../../instacart_data/products.csv")
    one = order_prior.groupby('order_id').agg({'add_to_cart_order':'max', 'product_id':'max'}).reset_index()
    one = one[one['add_to_cart_order'] == 1] 
    one = one.groupby('product_id').agg({'add_to_cart_order':'sum'}).reset_index().sort_values(by = 'add_to_cart_order', ascending = False)[:20]
    one = pd.merge(one, products, how= 'inner', on = 'product_id')
    return one

if __name__ == "__main__":
    pass
    color1 = '#F1D78C'
    color2 = '#F6A811'
    color3 = '#F46708'
    color4 = '#EF727F'
    color5 = '#E84846'
    citrus = [color1, color2, color3, color4, color5]

    one = get_one_item()
    make_bar(one, 'add_to_cart_order', 'product_name', 'Top Items For Single Orders', 
                'Number of Times Occurs as Only Item Ordered', 'Product Name')
    