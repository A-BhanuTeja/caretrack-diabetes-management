"""
Comprehensive Diet Plans for Diabetes Management
"""

def get_detailed_diet_plan(status, patient_age, bmi):
    """
    Generate detailed diet plan based on sugar status, age, and BMI
    
    Args:
        status: dict with 'fasting' and 'postmeal' sugar status
        patient_age: int - patient's age
        bmi: float - patient's BMI
    
    Returns:
        dict with comprehensive meal plans
    """
    
    # Determine overall condition
    if status['fasting'] == 'High' or status['postmeal'] == 'High':
        condition = 'high_sugar'
    elif status['fasting'] == 'Low':
        condition = 'low_sugar'
    else:
        condition = 'normal'
    
    # Base diet plan structure
    diet_plan = {
        'breakfast': [],
        'mid_morning_snack': [],
        'lunch': [],
        'evening_snack': [],
        'dinner': [],
        'bedtime_snack': [],
        'foods_to_eat': [],
        'foods_to_avoid': [],
        'general_tips': [],
        'hydration': [],
        'exercise': []
    }
    
    # HIGH SUGAR CONDITION
    if condition == 'high_sugar':
        diet_plan['breakfast'] = [
            {
                'name': 'Option 1: Oatmeal Bowl',
                'items': [
                    '1/2 cup steel-cut oats',
                    '1 cup unsweetened almond milk',
                    '1 tablespoon chia seeds',
                    '1/4 cup blueberries',
                    '5-6 almonds (crushed)',
                    '1/2 teaspoon cinnamon'
                ],
                'calories': '~300 cal',
                'why': 'High fiber keeps blood sugar stable'
            },
            {
                'name': 'Option 2: Vegetable Poha',
                'items': [
                    '1 cup flattened rice (poha)',
                    'Mixed vegetables (carrots, peas, beans)',
                    '1 teaspoon oil',
                    'Curry leaves, mustard seeds',
                    'Lemon juice'
                ],
                'calories': '~250 cal',
                'why': 'Light, nutritious, and diabetes-friendly'
            },
            {
                'name': 'Option 3: Moong Dal Cheela',
                'items': [
                    '1 cup moong dal batter',
                    'Chopped onions, tomatoes, green chili',
                    'Serve with mint chutney',
                    '1 cup green tea (unsweetened)'
                ],
                'calories': '~280 cal',
                'why': 'High protein controls hunger and sugar spikes'
            }
        ]
        
        diet_plan['mid_morning_snack'] = [
            '1 small apple with 10 almonds',
            '1 cup buttermilk (unsweetened)',
            '1/2 cup roasted chickpeas',
            'OR 1 small orange with 5 walnuts'
        ]
        
        diet_plan['lunch'] = [
            {
                'name': 'Complete Meal',
                'items': [
                    '2 small whole wheat rotis OR 1/2 cup brown rice',
                    '1 cup mixed vegetable curry (non-starchy)',
                    '1 cup dal (lentils)',
                    '1 cup cucumber-tomato salad',
                    '1/2 cup low-fat curd (yogurt)',
                    'Grilled chicken/fish (palm-sized portion) OR paneer'
                ],
                'calories': '~450-500 cal',
                'timing': '12:30 PM - 1:30 PM'
            }
        ]
        
        diet_plan['evening_snack'] = [
            '1 cup green tea with 2-3 whole grain biscuits',
            '1 small bowl sprouts salad',
            '1/2 cup roasted makhana (fox nuts)',
            'OR Mixed nuts (10-12 pieces)'
        ]
        
        diet_plan['dinner'] = [
            {
                'name': 'Light Dinner',
                'items': [
                    '2 small rotis OR 1 cup quinoa',
                    '1 cup green leafy vegetable (palak, methi)',
                    '1 cup clear vegetable soup',
                    'Grilled fish/chicken OR tofu',
                    'Salad with lemon dressing'
                ],
                'calories': '~400 cal',
                'timing': 'Before 8:00 PM',
                'note': 'Eat dinner at least 3 hours before bedtime'
            }
        ]
        
        diet_plan['bedtime_snack'] = [
            '1 cup warm turmeric milk (unsweetened)',
            'OR 5-6 almonds',
            'OR 1/2 cup low-fat curd'
        ]
        
        diet_plan['foods_to_eat'] = [
            '🥬 Leafy Greens: Spinach, kale, methi, amaranth',
            '🥦 Non-Starchy Vegetables: Broccoli, cauliflower, cabbage, beans, capsicum',
            '🌾 Whole Grains: Brown rice, quinoa, barley, whole wheat',
            '🥜 Nuts & Seeds: Almonds, walnuts, chia seeds, flax seeds',
            '🐟 Lean Proteins: Fish, chicken breast, eggs, tofu, paneer',
            '🫘 Legumes: Moong dal, chickpeas, kidney beans, lentils',
            '🫐 Low-Sugar Fruits: Berries, apple, guava, papaya, orange',
            '🥛 Dairy: Low-fat milk, curd, buttermilk (unsweetened)'
        ]
        
        diet_plan['foods_to_avoid'] = [
            '❌ White bread, white rice, maida products',
            '❌ Sugary drinks: Soda, fruit juices, energy drinks',
            '❌ Sweets: Cake, cookies, chocolates, ice cream',
            '❌ Fried foods: Samosa, pakora, French fries',
            '❌ Processed foods: Chips, instant noodles',
            '❌ High-sugar fruits: Mango, banana (ripe), grapes, custard apple',
            '❌ Full-fat dairy products',
            '❌ Red meat and processed meats',
            '❌ Alcohol'
        ]
        
        diet_plan['general_tips'] = [
            '⏰ Eat meals at the same time every day',
            '🍽️ Use smaller plates to control portions',
            '🐢 Eat slowly and chew thoroughly',
            '💧 Drink water 30 minutes before meals',
            '🚶 Walk for 10-15 minutes after each meal',
            '📊 Monitor blood sugar levels regularly',
            '🥗 Fill half your plate with vegetables',
            '🕐 Follow the 3-2-1 rule: 3 hours between meals, 2 hours before bed, 1 hour of exercise',
            '🧘 Practice stress management (yoga, meditation)',
            '😴 Get 7-8 hours of quality sleep'
        ]
        
        diet_plan['hydration'] = [
            '💧 Drink 8-10 glasses of water daily',
            '🍵 Green tea (2-3 cups) - no sugar',
            '🌿 Herbal teas: Cinnamon tea, fenugreek water',
            '🥤 Buttermilk (unsweetened)',
            '🥥 Coconut water (in moderation)',
            '❌ Avoid: Sugary drinks, packaged juices, alcohol'
        ]
        
        diet_plan['exercise'] = [
            '🚶 Morning walk: 30 minutes (before breakfast)',
            '🧘 Yoga: 15-20 minutes',
            '💪 Light strength training: 2-3 times a week',
            '🚴 Cycling or swimming: 3 times a week',
            '🏃 Post-meal walks: 10-15 minutes after each meal',
            '⚠️ Check blood sugar before and after exercise',
            '📅 Aim for 150 minutes of moderate activity per week'
        ]
    
    # LOW SUGAR CONDITION
    elif condition == 'low_sugar':
        diet_plan['breakfast'] = [
            {
                'name': 'Option 1: Quick Energy Breakfast',
                'items': [
                    '2 slices whole wheat bread with peanut butter',
                    '1 banana',
                    '1 glass milk with dates',
                    '2 boiled eggs'
                ],
                'calories': '~400 cal',
                'why': 'Quick carbs with protein prevent sugar drops'
            },
            {
                'name': 'Option 2: Indian Breakfast',
                'items': [
                    '2 parathas with curd',
                    '1 cup sweet lassi',
                    'Handful of raisins and dates'
                ],
                'calories': '~450 cal',
                'why': 'Balanced meal with sustained energy'
            }
        ]
        
        diet_plan['mid_morning_snack'] = [
            '1 banana with peanut butter',
            '1 glass fruit smoothie',
            'Handful of dates and nuts',
            'Energy bar'
        ]
        
        diet_plan['lunch'] = [
            {
                'name': 'Complete Meal',
                'items': [
                    '2-3 rotis OR 1 cup white/brown rice',
                    'Dal with ghee',
                    'Mixed vegetables',
                    'Chicken/fish curry',
                    'Salad',
                    '1 glass buttermilk'
                ],
                'calories': '~600 cal',
                'timing': 'Regular intervals - don\'t skip meals!'
            }
        ]
        
        diet_plan['evening_snack'] = [
            'Fruit juice with biscuits',
            'Sandwiches',
            'Sprouts salad with lemon',
            'Protein shake'
        ]
        
        diet_plan['dinner'] = [
            {
                'name': 'Nutritious Dinner',
                'items': [
                    '2-3 rotis OR rice',
                    'Paneer curry or chicken',
                    'Dal with ghee',
                    'Vegetables',
                    'Sweet dish (small portion)'
                ],
                'calories': '~500 cal',
                'note': 'Don\'t skip dinner'
            }
        ]
        
        diet_plan['bedtime_snack'] = [
            '1 glass milk with honey',
            'Handful of dry fruits',
            'Banana with dates'
        ]
        
        diet_plan['foods_to_eat'] = [
            '🍌 Fruits: Banana, mango, dates, raisins',
            '🍞 Whole grains with moderate portions',
            '🥛 Full-fat milk products',
            '🥜 Nuts: All types, especially dates and raisins',
            '🍯 Natural sweeteners: Honey, jaggery (in moderation)',
            '🥔 Starchy vegetables: Potato, sweet potato',
            '🍝 Complex carbs: Pasta, rice, bread',
            '🥩 Protein: Eggs, chicken, fish, paneer'
        ]
        
        diet_plan['foods_to_avoid'] = [
            '❌ Skipping meals',
            '❌ Excessive caffeine',
            '❌ Alcohol on empty stomach',
            '❌ Very long gaps between meals',
            '❌ Over-exercising without eating'
        ]
        
        diet_plan['general_tips'] = [
            '⏰ NEVER skip meals - eat every 2-3 hours',
            '🍬 Carry glucose tablets or candy',
            '📱 Keep family informed about your condition',
            '⚠️ Recognize low sugar symptoms: Shakiness, sweating, confusion',
            '🍪 Always carry emergency snacks',
            '📊 Check blood sugar frequently',
            '💊 Take medications with food',
            '🚫 Avoid prolonged fasting',
            '🏃 Don\'t exercise on empty stomach',
            '😴 Eat a bedtime snack if sugar is low'
        ]
    
    # NORMAL CONDITION
    else:
        diet_plan['breakfast'] = [
            {
                'name': 'Balanced Breakfast',
                'items': [
                    'Oats with milk and fruits',
                    'OR 2 rotis with vegetables',
                    'OR Egg white omelet with toast',
                    '1 cup green tea'
                ],
                'calories': '~300-350 cal',
                'why': 'Maintains stable blood sugar'
            }
        ]
        
        diet_plan['mid_morning_snack'] = [
            'Fresh fruit with nuts',
            'Green tea with biscuits',
            'Buttermilk'
        ]
        
        diet_plan['lunch'] = [
            {
                'name': 'Balanced Meal',
                'items': [
                    '2 rotis OR 3/4 cup rice',
                    'Dal',
                    'Vegetable curry',
                    'Salad',
                    'Curd',
                    'Protein (chicken/fish/paneer)'
                ],
                'calories': '~450-500 cal'
            }
        ]
        
        diet_plan['evening_snack'] = [
            'Tea/coffee with healthy snacks',
            'Fruits',
            'Nuts',
            'Roasted chickpeas'
        ]
        
        diet_plan['dinner'] = [
            {
                'name': 'Light Dinner',
                'items': [
                    '2 rotis OR soup with bread',
                    'Light curry',
                    'Salad',
                    'Grilled protein'
                ],
                'calories': '~400 cal'
            }
        ]
        
        diet_plan['general_tips'] = [
            '✅ You\'re doing great! Keep it up!',
            '⏰ Maintain regular meal timings',
            '🥗 Continue balanced diet',
            '🏃 Keep exercising regularly',
            '📊 Monitor sugar levels weekly',
            '💧 Stay hydrated',
            '😴 Get adequate sleep',
            '🧘 Manage stress levels'
        ]
    
    # Adjust for BMI
    if bmi > 30:
        diet_plan['bmi_note'] = 'Your BMI indicates obesity. Focus on portion control and regular exercise. Consult a nutritionist for personalized plan.'
    elif bmi > 25:
        diet_plan['bmi_note'] = 'Your BMI indicates overweight. Reduce portion sizes and increase physical activity.'
    elif bmi < 18.5:
        diet_plan['bmi_note'] = 'Your BMI indicates underweight. Increase calorie intake with nutritious foods. Consider consulting a doctor.'
    
    # Adjust for age
    if patient_age > 60:
        diet_plan['age_note'] = 'Senior citizens need: More calcium (milk, curd), easy-to-digest foods, vitamin D supplements, and regular health checkups.'
    elif patient_age < 30:
        diet_plan['age_note'] = 'Young adults: Focus on building healthy habits now for long-term diabetes management.'
    
    return diet_plan


def get_indian_meal_alternatives():
    """Common Indian meal alternatives for diabetes"""
    return {
        'breakfast': {
            'avoid': ['Aloo paratha', 'Poori-bhaji', 'Sweet dosa'],
            'choose': ['Oats upma', 'Moong dal cheela', 'Ragi dosa', 'Vegetable poha']
        },
        'lunch_dinner': {
            'avoid': ['White rice', 'Naan', 'Fried items'],
            'choose': ['Brown rice', 'Jowar roti', 'Bajra roti', 'Ragi roti']
        },
        'snacks': {
            'avoid': ['Samosa', 'Pakora', 'Namkeen', 'Biscuits'],
            'choose': ['Roasted chana', 'Makhana', 'Sprouts', 'Roasted peanuts']
        }
    }