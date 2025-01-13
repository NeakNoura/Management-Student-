import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_faqs(cvs_path):
    try:
        data = pd.read_csv(csv_path)
        if "Question"not in data.columns or 'Response'not in data.columns:
            raise ValueError("CSV file must contain 'Question and Response' columns. " )
        return data 
    except Exception as e:
        print(f"Error loading FAQS: {e}")
        return pd.DataFrame(columns=['Question', 'Response'])
    
    
def show_faqs(data):
    if data.empty:
        print('No FAQS available')
        return
    print("\nFrequently Asked Questions:")
    for i, row in data.iterrows():
        print(f"{i+i}.{row['Questions']}")
    print("\nEnter the number of the question you'd like to know more about or type 'back' to return.")
    while True :
        user_input = input ('Your choice :').strip()
        if user_input.lower()== 'back':
            break
        try :
            choice = int(user_input)-1
            if 0 <= choice < len(data):
                print(f"\n{data.iloc[choice]['Question']} \nBot: {data.iloc[choice]['Response']}\n")
            else:
                print('Invalid choice . PLease try again')
        except ValueError:
            print('Invalid input. Please enter a number.')
            
            
            
def evaluate_model(model, x_test, y_test):
    try:
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test,x_test)
        print(f"Model accuracy: {accuracy * 100:.2f}%")
        return accuracy
    except Exception as e:
        print(f"Error during evaluation: {e}")
        return 0.0
        
    
def interact_with_chatbot(model, faqs_data):
    print("\nChatbot is ready ! Type 'exit' to quit or 'faq' to check FAQS.")
    while True:
        user_input = input('you:')
        if user_input.strip().lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.strip().lower() == 'faq':
            show_faqs(faqs_data)
        else:
            try:
                response = model.predict([user_input])[0]
                print(f"Bot: {response}")
            except Exception as e:
                print (f"Error generation response: {e}")
                
                
if __name__ == "__main__":
    csv_path = r"D:\Computer Science\Interlligent System Development\AI_Aoutomatic.csv"
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found in the CSV file.")
        exit()
    data = load_faqs(csv_path)
    if data.empty:
        print("No valid data found in the CSV file.")
        exit()
    x=data["Question"]
    y=data["Response"]
    
    x_train,x_test,y_train ,y_test= train_test_split(x,y,test_size=0.2, random_state=42)
    print('Training the model...')
    model =  make_pipeline(
        CountVectorizer(stop_words="english"),
        LogisticRegression(max_iter=1000,solver='liblinear')
        
    )
    model.fit(x_train, y_train)
    
    
    accuracy = evaluate_model(model,x_test,y_test)
    if accuracy < 0.8:
        print("waning : Model accuracy is below 80% . Consider improving the dataset. ")
    
    interact_with_chatbot(model, data)