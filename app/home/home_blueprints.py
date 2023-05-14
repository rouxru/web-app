from flask import Blueprint, render_template, request, redirect
from app.home.models import Data
from app import db

# Blueprint Configuration
home_blueprints = Blueprint(
    "home_blueprints", __name__, template_folder="templates", static_folder="static"
)


@home_blueprints.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == 'POST':
        Type = request.form.get('type')
        Model = request.form.get('model')
        Characteristics = request.form.get('Characteristics')
        staff = request.form.get('staff')
        Location = request.form.get('Location')
        Status = request.form.get('Status')
        MAC = request.form.get('Address')
        Name = request.form.get('Name')
        Inventory = request.form.get('Inventory')
        Graphics = request.form.get('Graphics')
        Comments = request.form.get('Comments')
        Serial = request.form.get('Serial')
        username = request.form.get('username')
        warranty = request.form.get('warranty')
        Order = request.form.get('Order')

        Record = Data(Type=Type, Model=Model, Characteristics=Characteristics, staff=staff,
                      Location=Location, Status=Status, MAC=MAC,
                      Name=Name, Inventory=Inventory, Graphics=Graphics,
                      Comments=Comments, Serial=Serial, username=username, warranty=warranty,
                      Order=Order
                      )

        db.session.add(Record)
        db.session.commit()

    """Render home page"""
    return render_template(
        "index.html",
    )


@home_blueprints.route("/edit/<id>", methods=["GET", "POST"])
def Edit_Record(id):
    Record = Data.query.filter_by(id=id).first()
    if request.method == 'POST':
        Type = request.form.get('type')
        Model = request.form.get('model')
        Characteristics = request.form.get('Characteristics')
        staff = request.form.get('staff')
        Location = request.form.get('Location')
        Status = request.form.get('Status')
        MAC = request.form.get('Address')
        Name = request.form.get('Name')
        Inventory = request.form.get('Inventory')
        Graphics = request.form.get('Graphics')
        Comments = request.form.get('Comments')
        Serial = request.form.get('Serial')
        username = request.form.get('username')
        warranty = request.form.get('warranty')
        Order = request.form.get('Order')

        Record.Type = Type
        Record.Model = Model
        Record.Characteristics = Characteristics
        Record.staff = staff
        Record.Location = Location
        Record.Status = Status
        Record.MAC = MAC
        Record.Name = Name
        Record.Inventory = Inventory
        Record.Graphics = Graphics
        Record.Comments = Comments
        Record.Serial = Serial
        Record.username = username
        Record.warranty = warranty
        Record.Order = Order

        db.session.add(Record)
        db.session.commit()

    """Render edit page."""
    return render_template(
        "edit.html",
        Record=Record
    )


@home_blueprints.route("/delete/<id>", methods=["GET", "POST"])
def delete_Record(id):
    Record = Data.query.filter_by(id=id).first()
    db.session.delete(Record)
    db.session.commit()
    return redirect('/')


@home_blueprints.route("/view", methods=["GET", "POST"])
def view_Record():
    Record = Data.query.all()

    """Render the view page"""
    return render_template(
        "view.html",
        Record=Record
    )
