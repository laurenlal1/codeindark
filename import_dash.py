import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Mock Data - Simulates data scraped from parts.cat.com
# In a real application, this data would be fetched from a backend API
# that handles the actual web scraping or database queries.
mock_data = {
    "equipmentTypes": [
        {
            "id": "excavators",
            "name": "Excavators",
            "recommendedParts": [
                {
                    "partNumber": "336-1234",
                    "description": "Hydraulic Filter Kit (Standard Maintenance)",
                    "imageUrl": "https://placehold.co/150x100/FF0000/FFFFFF?text=Hydraulic+Filter",
                    "price": 125.50,
                    "availability": "In Stock",
                    "quantityAvailable": 150,
                    "category": "Filters",
                    "popularityScore": 85
                },
                {
                    "partNumber": "452-5678",
                    "description": "Engine Oil Filter (Advanced Performance)",
                    "imageUrl": "https://placehold.co/150x100/0000FF/FFFFFF?text=Engine+Filter",
                    "price": 89.99,
                    "availability": "Low Stock",
                    "quantityAvailable": 25,
                    "category": "Filters",
                    "popularityScore": 78
                },
                {
                    "partNumber": "901-7890",
                    "description": "Track Link Assembly (Heavy Duty)",
                    "imageUrl": "https://placehold.co/150x100/00FF00/FFFFFF?text=Track+Link",
                    "price": 1250.00,
                    "availability": "In Stock",
                    "quantityAvailable": 10,
                    "category": "Undercarriage",
                    "popularityScore": 60
                },
                {
                    "partNumber": "210-1122",
                    "description": "Bucket Teeth Kit (Standard)",
                    "imageUrl": "https://placehold.co/150x100/FFFF00/000000?text=Bucket+Teeth",
                    "price": 320.75,
                    "availability": "In Stock",
                    "quantityAvailable": 75,
                    "category": "Ground Engaging Tools",
                    "popularityScore": 92
                },
                {
                    "partNumber": "777-3344",
                    "description": "Hydraulic Cylinder Seal Kit",
                    "imageUrl": "https://placehold.co/150x100/800080/FFFFFF?text=Seal+Kit",
                    "price": 180.25,
                    "availability": "Out of Stock",
                    "quantityAvailable": 0,
                    "category": "Hydraulics",
                    "popularityScore": 55
                },
                {
                    "partNumber": "600-0010",
                    "description": "Excavator Boom Pin",
                    "imageUrl": "https://placehold.co/150x100/333333/FFFFFF?text=Boom+Pin",
                    "price": 450.00,
                    "availability": "In Stock",
                    "quantityAvailable": 30,
                    "category": "Structural Components",
                    "popularityScore": 70
                },
                {
                    "partNumber": "700-0020",
                    "description": "Swing Bearing Assembly",
                    "imageUrl": "https://placehold.co/150x100/666666/FFFFFF?text=Swing+Bearing",
                    "price": 3500.00,
                    "availability": "Low Stock",
                    "quantityAvailable": 3,
                    "category": "Structural Components",
                    "popularityScore": 65
                }
            ]
        },
        {
            "id": "dozers",
            "name": "Dozers",
            "recommendedParts": [
                {
                    "partNumber": "888-9900",
                    "description": "Cutting Edge (D6 Dozer)",
                    "imageUrl": "https://placehold.co/150x100/FFA500/FFFFFF?text=Cutting+Edge",
                    "price": 550.00,
                    "availability": "In Stock",
                    "quantityAvailable": 40,
                    "category": "Ground Engaging Tools",
                    "popularityScore": 88
                },
                {
                    "partNumber": "123-4567",
                    "description": "Final Drive Seal Group",
                    "imageUrl": "https://placehold.co/150x100/FFC0CB/000000?text=Final+Drive+Seal",
                    "price": 280.99,
                    "availability": "Low Stock",
                    "quantityAvailable": 10,
                    "category": "Drivetrain",
                    "popularityScore": 70
                },
                {
                    "partNumber": "654-3210",
                    "description": "Undercarriage Roller",
                    "imageUrl": "https://placehold.co/150x100/00FFFF/000000?text=Undercarriage+Roller",
                    "price": 410.00,
                    "availability": "In Stock",
                    "quantityAvailable": 60,
                    "category": "Undercarriage",
                    "popularityScore": 75
                },
                {
                    "partNumber": "987-6543",
                    "description": "Fuel Filter Assembly",
                    "imageUrl": "https://placehold.co/150x100/ADD8E6/000000?text=Fuel+Filter",
                    "price": 75.25,
                    "availability": "In Stock",
                    "quantityAvailable": 120,
                    "category": "Filters",
                    "popularityScore": 82
                },
                {
                    "partNumber": "DZR-1001",
                    "description": "Ripper Shank",
                    "imageUrl": "https://placehold.co/150x100/8B4513/FFFFFF?text=Ripper+Shank",
                    "price": 980.00,
                    "availability": "In Stock",
                    "quantityAvailable": 20,
                    "category": "Ground Engaging Tools",
                    "popularityScore": 68
                },
                {
                    "partNumber": "DZR-1002",
                    "description": "Blade Tilt Cylinder",
                    "imageUrl": "https://placehold.co/150x100/40E0D0/000000?text=Blade+Cylinder",
                    "price": 1500.00,
                    "availability": "Out of Stock",
                    "quantityAvailable": 0,
                    "category": "Hydraulics",
                    "popularityScore": 50
                }
            ]
        },
        {
            "id": "wheel-loaders",
            "name": "Wheel Loaders",
            "recommendedParts": [
                {
                    "partNumber": "555-6677",
                    "description": "Bucket Edge Bolt Kit",
                    "imageUrl": "https://placehold.co/150x100/C0C0C0/000000?text=Bolt+Kit",
                    "price": 95.00,
                    "availability": "In Stock",
                    "quantityAvailable": 90,
                    "category": "Ground Engaging Tools",
                    "popularityScore": 80
                },
                {
                    "partNumber": "112-2334",
                    "description": "Brake Pad Set (Front)",
                    "imageUrl": "https://placehold.co/150x100/A52A2A/FFFFFF?text=Brake+Pads",
                    "price": 210.50,
                    "availability": "Low Stock",
                    "quantityAvailable": 15,
                    "category": "Brakes",
                    "popularityScore": 72
                },
                {
                    "partNumber": "445-5667",
                    "description": "Transmission Filter",
                    "imageUrl": "https://placehold.co/150x100/4B0082/FFFFFF?text=Transmission+Filter",
                    "price": 65.75,
                    "availability": "In Stock",
                    "quantityAvailable": 80,
                    "category": "Filters",
                    "popularityScore": 70
                },
                {
                    "partNumber": "332-1100",
                    "description": "Steering Cylinder Seal Kit",
                    "imageUrl": "https://placehold.co/150x100/FFD700/000000?text=Steering+Seal+Kit",
                    "price": 150.00,
                    "availability": "In Stock",
                    "quantityAvailable": 30,
                    "category": "Hydraulics",
                    "popularityScore": 65
                },
                {
                    "partNumber": "WHL-2001",
                    "description": "Wheel Loader Tire (Single)",
                    "imageUrl": "https://placehold.co/150x100/778899/FFFFFF?text=Loader+Tire",
                    "price": 1800.00,
                    "availability": "In Stock",
                    "quantityAvailable": 8,
                    "category": "Tires",
                    "popularityScore": 90
                }
            ]
        },
        {
            "id": "articulated-trucks",
            "name": "Articulated Trucks",
            "recommendedParts": [
                {
                    "partNumber": "789-0123",
                    "description": "Air Filter Element (Primary)",
                    "imageUrl": "https://placehold.co/150x100/2E8B57/FFFFFF?text=Air+Filter",
                    "price": 110.00,
                    "availability": "In Stock",
                    "quantityAvailable": 100,
                    "category": "Filters",
                    "popularityScore": 90
                },
                {
                    "partNumber": "009-8877",
                    "description": "Suspension Bushing",
                    "imageUrl": "https://placehold.co/150x100/DC143C/FFFFFF?text=Suspension+Bushing",
                    "price": 70.00,
                    "availability": "Low Stock",
                    "quantityAvailable": 5,
                    "category": "Suspension",
                    "popularityScore": 68
                },
                {
                    "partNumber": "223-3445",
                    "description": "Brake Chamber",
                    "imageUrl": "https://placehold.co/150x100/6A5ACD/FFFFFF?text=Brake+Chamber",
                    "price": 380.00,
                    "availability": "In Stock",
                    "quantityAvailable": 20,
                    "category": "Brakes",
                    "popularityScore": 75
                },
                {
                    "partNumber": "ART-3001",
                    "description": "Dump Body Liner Kit",
                    "imageUrl": "https://placehold.co/150x100/DAA520/000000?text=Body+Liner",
                    "price": 2500.00,
                    "availability": "In Stock",
                    "quantityAvailable": 5,
                    "category": "Body Components",
                    "popularityScore": 60
                }
            ]
        },
        {
            "id": "skid-steer-loaders",
            "name": "Skid Steer Loaders",
            "recommendedParts": [
                {
                    "partNumber": "100-2000",
                    "description": "Hydraulic Quick Coupler Set",
                    "imageUrl": "https://placehold.co/150x100/FF6347/FFFFFF?text=Quick+Coupler",
                    "price": 450.00,
                    "availability": "In Stock",
                    "quantityAvailable": 30,
                    "category": "Attachments",
                    "popularityScore": 85
                },
                {
                    "partNumber": "500-6000",
                    "description": "Drive Belt Kit",
                    "imageUrl": "https://placehold.co/150x100/4682B4/FFFFFF?text=Drive+Belt",
                    "price": 120.00,
                    "availability": "In Stock",
                    "quantityAvailable": 50,
                    "category": "Engine",
                    "popularityScore": 70
                },
                {
                    "partNumber": "700-8000",
                    "description": "Skid Steer Tires (Set of 4)",
                    "imageUrl": "https://placehold.co/150x100/D2B48C/000000?text=Skid+Steer+Tires",
                    "price": 980.00,
                    "availability": "Low Stock",
                    "quantityAvailable": 5,
                    "category": "Tires",
                    "popularityScore": 95
                },
                {
                    "partNumber": "SKD-4001",
                    "description": "Bucket Cylinder Seal",
                    "imageUrl": "https://placehold.co/150x100/9ACD32/000000?text=Bucket+Seal",
                    "price": 85.00,
                    "availability": "In Stock",
                    "quantityAvailable": 45,
                    "category": "Hydraulics",
                    "popularityScore": 78
                }
            ]
        }
    ],
    "partCategories": [
        "Filters",
        "Undercarriage",
        "Ground Engaging Tools",
        "Hydraulics",
        "Drivetrain",
        "Brakes",
        "Suspension",
        "Attachments",
        "Engine",
        "Tires",
        "Structural Components",
        "Body Components"
    ]
}

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css'])

# Define the layout of the dashboard
app.layout = html.Div(
    className="min-h-screen bg-gray-100 font-['Inter'] p-4 sm:p-8",
    children=[
        # Header
        html.Header(
            # Updated header gradient colors
            className="bg-gradient-to-r from-[#50748A] to-[#FFC412] text-white p-6 rounded-xl shadow-lg mb-8 text-center",
            children=[
                html.H1("Cat Parts Dashboard", className="text-3xl sm:text-4xl font-bold mb-2"),
                html.P("Customized Experience for Your Equipment", className="text-lg sm:text-xl opacity-90"),
            ],
        ),

        # Equipment Type Toggle
        html.Section(
            className="mb-8 bg-white p-6 rounded-lg shadow-md",
            children=[
                html.H2("Select Equipment Type", className="text-2xl font-semibold text-gray-800 mb-4 text-center"),
                html.Div(
                    className="flex flex-wrap justify-center gap-3",
                    children=[
                        html.Button(
                            eq["name"],
                            id={"type": "equipment-button", "index": eq["id"]},
                            # Updated button active state color
                            className="px-6 py-3 rounded-full text-lg font-medium transition-all duration-300 ease-in-out bg-gray-200 text-gray-700 hover:bg-gray-300 hover:text-gray-800 focus:outline-none focus:ring-2 focus:ring-[#FFC412] focus:ring-opacity-75",
                            n_clicks=0,
                        )
                        for eq in mock_data["equipmentTypes"]
                    ],
                ),
                dcc.Store(id='selected-equipment-store', data=mock_data["equipmentTypes"][0]["id"]) # Store for selected equipment ID
            ],
        ),

        # Main Content Area (will be updated by callbacks)
        html.Main(id="main-content-area"),

        # Footer
        html.Footer(
            className="text-center text-gray-600 mt-12 p-4",
            children=[
                html.P(f"© {pd.Timestamp.now().year} Cat Parts Dashboard. All rights reserved. (Mock Data)"),
                html.P(
                    "This dashboard uses simulated data and is for demonstration purposes only. It does not connect to live Cat systems.",
                    className="text-sm mt-2",
                ),
            ],
        ),
    ],
)

# Callback to update the selected equipment ID in the store
@app.callback(
    Output('selected-equipment-store', 'data'),
    [Input({"type": "equipment-button", "index": dash.ALL}, "n_clicks")],
    prevent_initial_call=True
)
def update_selected_equipment_store(n_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    selected_id = eval(button_id)["index"] # Safely evaluate the stringified dict

    return selected_id

# Callback to update button styles based on selection
@app.callback(
    [Output({"type": "equipment-button", "index": eq["id"]}, "className") for eq in mock_data["equipmentTypes"]],
    [Input('selected-equipment-store', 'data')]
)
def update_button_styles(selected_equipment_id):
    button_classes = []
    base_class = "px-6 py-3 rounded-full text-lg font-medium transition-all duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-[#FFC412] focus:ring-opacity-75"
    for eq in mock_data["equipmentTypes"]:
        if eq["id"] == selected_equipment_id:
            button_classes.append(f"{base_class} bg-[#FFC412] text-white shadow-md transform scale-105")
        else:
            button_classes.append(f"{base_class} bg-gray-200 text-gray-700 hover:bg-gray-300 hover:text-gray-800")
    return button_classes

# Callback to update the main content area (recommended parts and charts)
@app.callback(
    Output("main-content-area", "children"),
    [Input("selected-equipment-store", "data")],
)
def update_main_content(selected_equipment_id):
    current_equipment = next((eq for eq in mock_data["equipmentTypes"] if eq["id"] == selected_equipment_id), None)

    if not current_equipment:
        return html.Div(html.P("No equipment selected or data not found.", className="text-center text-gray-500 mt-16"))

    # Prepare data for "Availability Breakdown by Part Category" chart
    availability_counts = {}
    for part in current_equipment["recommendedParts"]:
        availability_counts.setdefault(part["category"], {'In Stock': 0, 'Low Stock': 0, 'Out of Stock': 0})
        availability_counts[part["category"]][part["availability"]] += 1

    availability_data_list = []
    for category, counts in availability_counts.items():
        availability_data_list.append({
            'category': category,
            'In Stock': counts['In Stock'],
            'Low Stock': counts['Low Stock'],
            'Out of Stock': counts['Out of Stock'],
            'total': counts['In Stock'] + counts['Low Stock'] + counts['Out of Stock']
        })
    availability_df = pd.DataFrame(availability_data_list)

    # Prepare data for "Top Recommended Parts by Sales Volume (Simulated)" chart
    top_parts_data_list = sorted(
        current_equipment["recommendedParts"], key=lambda x: x["popularityScore"], reverse=True
    )[:5]
    top_parts_df = pd.DataFrame([
        {"partName": part["description"].split('(')[0].strip(), "popularity": part["popularityScore"]}
        for part in top_parts_data_list
    ])

    # Create Availability Breakdown Chart (Stacked Bar Chart)
    if not availability_df.empty:
        # Melt the DataFrame for stacked bar chart
        availability_melted_df = availability_df.melt(
            id_vars=['category'],
            value_vars=['In Stock', 'Low Stock', 'Out of Stock'],
            var_name='Availability Status',
            value_name='Count'
        )
        availability_fig = px.bar(
            availability_melted_df,
            x='category',
            y='Count',
            color='Availability Status',
            title='Availability Breakdown by Part Category',
            labels={'category': 'Part Category', 'Count': 'Number of Parts'},
            # Updated chart colors for availability
            color_discrete_map={
                'In Stock': '#50748A', # Muted Blue/Grey
                'Low Stock': '#FFC412', # Vibrant Yellow/Orange
                'Out of Stock': '#333333' # Dark Grey
            }
        )
        availability_fig.update_layout(
            font_family="Inter",
            title_font_size=20,
            title_x=0.5,
            margin=dict(l=40, r=40, t=60, b=40),
            paper_bgcolor='white',
            plot_bgcolor='white',
            legend_title_text='Status',
        )
    else:
        availability_fig = go.Figure()
        availability_fig.add_annotation(
            text="No data available for this chart.",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="gray")
        )
        availability_fig.update_layout(
            title='Availability Breakdown by Part Category',
            title_font_size=20,
            title_x=0.5,
            height=300,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )


    # Create Top Recommended Parts Chart
    if not top_parts_df.empty:
        top_parts_fig = px.bar(
            top_parts_df,
            x='partName',
            y='popularity',
            title='Top Recommended Parts by Popularity (Simulated)',
            labels={'partName': 'Part Name', 'popularity': 'Popularity Score'},
            # Updated chart color for popularity
            color_discrete_sequence=['#FFC412'] # Vibrant Yellow/Orange
        )
        top_parts_fig.update_layout(
            font_family="Inter",
            title_font_size=20,
            title_x=0.5,
            margin=dict(l=40, r=40, t=60, b=40),
            paper_bgcolor='white',
            plot_bgcolor='white',
        )
    else:
        top_parts_fig = go.Figure()
        top_parts_fig.add_annotation(
            text="No data available for this chart.",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="gray")
        )
        top_parts_fig.update_layout(
            title='Top Recommended Parts by Popularity (Simulated)',
            title_font_size=20,
            title_x=0.5,
            height=300,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )


    return html.Div(
        children=[
            # Recommended Parts Section
            html.Section(
                className="mb-8",
                children=[
                    html.H2(
                        f"Recommended Parts for {current_equipment['name']}",
                        className="text-2xl font-semibold text-gray-800 mb-6 text-center",
                    ),
                    html.Div(
                        className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
                        children=[
                            html.Div(
                                key=part["partNumber"],
                                className="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-200 hover:scale-105",
                                children=[
                                    html.Img(
                                        src=part["imageUrl"],
                                        alt=part["description"],
                                        className="w-full h-40 object-cover",
                                    ),
                                    html.Div(
                                        className="p-5",
                                        children=[
                                            html.H3(
                                                part["description"],
                                                className="text-lg font-bold text-gray-900 mb-2 truncate",
                                                title=part["description"],
                                            ),
                                            html.P(
                                                html.Span("Part #: ", className="font-semibold"),
                                                part["partNumber"],
                                                className="text-sm text-gray-600 mb-1",
                                            ),
                                            html.P(
                                                html.Span("Category: ", className="font-semibold"),
                                                part["category"],
                                                className="text-sm text-gray-600 mb-1",
                                            ),
                                            html.P(
                                                f"${part['price']:.2f}",
                                                className="text-xl font-bold text-[#50748A] mb-2", # Price color updated
                                            ),
                                            html.P(
                                                [
                                                    html.Span("Availability: ", className="font-semibold"),
                                                    html.Span(
                                                        f"{part['availability']} {f'({part['quantityAvailable']})' if part['availability'] != 'Out of Stock' else ''}",
                                                        # Updated availability status colors
                                                        className=f"ml-2 px-2 py-1 rounded-full text-white text-xs "
                                                        f"{'bg-gray-700' if part['availability'] == 'In Stock' else ''}"
                                                        f"{'bg-gray-500' if part['availability'] == 'Low Stock' else ''}"
                                                        f"{'bg-black' if part['availability'] == 'Out of Stock' else ''}",
                                                    ),
                                                ],
                                                className="text-sm font-semibold",
                                            ),
                                        ],
                                    ),
                                ],
                            )
                            for part in current_equipment["recommendedParts"]
                        ],
                    ),
                ],
            ),

            # Charts Section
            html.Section(
                children=[
                    html.H2(
                        f"Insights for {current_equipment['name']} Parts",
                        className="text-2xl font-semibold text-gray-800 mb-6 text-center",
                    ),
                    # Availability Breakdown Chart
                    html.Div(
                        className="bg-white p-6 rounded-lg shadow-md mb-8",
                        children=[
                            dcc.Graph(figure=availability_fig)
                        ]
                    ),
                    html.Div(
                        className="bg-white p-6 rounded-lg shadow-md mb-8",
                        children=[
                            html.H3("Availability Details", className="text-xl font-semibold text-gray-800 mb-4 text-center"),
                            html.Div(
                                className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4",
                                children=[
                                    html.Div(
                                        className="p-4 border rounded-md bg-gray-50",
                                        children=[
                                            html.P(f"{data['category']}", className="font-bold text-gray-800 mb-1"),
                                            html.P(f"In Stock: {data['In Stock']}", className="text-sm text-gray-700"), # Text color updated
                                            html.P(f"Low Stock: {data['Low Stock']}", className="text-sm text-gray-500"), # Text color updated
                                            html.P(f"Out of Stock: {data['Out of Stock']}", className="text-sm text-black"), # Text color updated
                                        ]
                                    ) for data in availability_data_list
                                ]
                            ) if availability_data_list else html.P("No availability data available.", className="text-center text-gray-500")
                        ]
                    ),


                    # Top Recommended Parts Chart
                    html.Div(
                        className="bg-white p-6 rounded-lg shadow-md mb-8",
                        children=[
                            dcc.Graph(figure=top_parts_fig)
                        ]
                    ),
                ],
            ),
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)
