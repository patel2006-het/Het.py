# Accept contact details from the user and create a vcard that we can directly store in our mobile.
# This program asks for your contact details and creates a vCard file (.vcf)
# which can be imported into your phone's contacts.

# Ask the user for their contact information
full_name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")

company = input("Enter company/organization (optional): ")
address = input("Enter address (optional): ")


# Create the vCard text
vcard = "BEGIN:VCARD\n"
vcard += "VERSION:3.0\n"
vcard += f"FN:{full_name}\n"
vcard += f"mobile number:{phone}\n"
vcard += f"EMAIL:{email}\n"

if company:
    vcard += f"ORG:{company}\n"

if address:
    vcard += f"ADR:{address}\n"

vcard += "END:VCARD\n"

# Save the vCard to a .vcf file
file_name = full_name.replace(" ", "_") + ".vcf"  # file name will be like John_Doe.vcf
with open(file_name, "w") as f:
    f.write(vcard)

print(f"\n Your vCard has been saved as '{file_name}'. You can import this into your phone's contacts.")
