# Streamlit UI for CRUD Project

import streamlit as st
from pathlib import Path
import os

st.title("CRUD File Management System")

# ---------- FUNCTIONS ----------

def create_file(file_name, content):
    p = Path(file_name)

    if p.exists():
        return "File already exists..."

    with open(file_name, 'w') as file:
        file.write(content)

    return "File created successfully..."


def read_file(file_name):
    p = Path(file_name)

    if p.exists():
        with open(file_name, 'r') as file:
            return file.read()

    return "File does not exist..."


def update_file(file_name, content, mode):
    p = Path(file_name)

    if not p.exists():
        return "File does not exist..."

    if mode == "Append":
        with open(file_name, 'a') as file:
            file.write(content)

        return "File updated successfully..."

    elif mode == "Overwrite":
        with open(file_name, 'w') as file:
            file.write(content)

        return "File overwritten successfully..."


def delete_file(file_name):
    p = Path(file_name)

    if p.exists():
        os.remove(p)
        return "File deleted successfully..."

    return "File does not exist..."


def rename_file(old_name, new_name):
    p = Path(old_name)

    if p.exists():
        p.rename(new_name)
        return "File renamed successfully..."

    return "File does not exist..."


# ---------- SIDEBAR ----------

option = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File"
    ]
)


# ---------- CREATE ----------

if option == "Create File":
    st.header("Create File")

    file_name = st.text_input("Enter File Name")
    content = st.text_area("Enter File Content")

    if st.button("Create"):
        result = create_file(file_name, content)
        st.success(result)


# ---------- READ ----------

elif option == "Read File":
    st.header("Read File")

    file_name = st.text_input("Enter File Name")

    if st.button("Read"):
        result = read_file(file_name)
        st.text(result)


# ---------- UPDATE ----------

elif option == "Update File":
    st.header("Update File")

    file_name = st.text_input("Enter File Name")

    mode = st.radio("Select Mode", ["Append", "Overwrite"])

    content = st.text_area("Enter Content")

    if st.button("Update"):
        result = update_file(file_name, content, mode)
        st.success(result)


# ---------- DELETE ----------

elif option == "Delete File":
    st.header("Delete File")

    file_name = st.text_input("Enter File Name")

    if st.button("Delete"):
        result = delete_file(file_name)
        st.success(result)


# ---------- RENAME ----------

elif option == "Rename File":
    st.header("Rename File")

    old_name = st.text_input("Enter Old File Name")
    new_name = st.text_input("Enter New File Name")

    if st.button("Rename"):
        result = rename_file(old_name, new_name)
        st.success(result)
