
#ads token limk https://ui.adsabs.harvard.edu/user/settings/token

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x170")
root.resizable(False, False)
root.title('Astro MVP')

# store keyword address and pub_year
keyword = tk.StringVar()
ads = tk.StringVar()

# submit frame
submit_frame = ttk.Frame(root)
submit_frame.pack(padx=10, pady=10, fill='x', expand=True)

#ADS 
ADS_label = ttk.Label(submit_frame, text="ADS Token:")
ADS_label.pack(fill='x', expand=True)

ADS_entry = ttk.Entry(submit_frame, textvariable=ads)
ADS_entry.pack(fill='x', expand=True)
ADS_entry.focus()

# keywords
keyword_label = ttk.Label(submit_frame, text="Keyword(s):")
keyword_label.pack(fill='x', expand=True)

keyword_entry = ttk.Entry(submit_frame, textvariable=keyword)
keyword_entry.pack(fill='x', expand=True)
keyword_entry.focus()

#To add a search option for the publication year 
# pub_year
# pub_year_label = ttk.Label(submit_frame, text="Publication Year:")
# pub_year_label.pack(fill='x', expand=True)

# pub_year_entry = ttk.Entry(submit_frame, textvariable=pub_year, show="*")
# pub_year_entry.pack(fill='x', expand=True)


#THIS IS WHERE YOU GRAB THE VAlUES SUMBMITTED IN THE TEXTBOX
keyword_input,token_input = [],[]
def submit_clicked():
    keyword_input.append(keyword.get())
    token_input.append(ads.get())
    root.destroy()
    return keyword_input,token_input 



submit_button = ttk.Button(submit_frame, text="Submit", command=submit_clicked)
submit_button.pack(fill='x', expand=True, pady=10)

root.mainloop()