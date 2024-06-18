import streamlit as st

def hello_world():
    return "Hello, World! Aula de docker"

def main():
    st.write(hello_world())

if __name__ == "__main__":
    main()