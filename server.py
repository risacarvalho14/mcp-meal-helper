from mcp.server.mcpserver import MCPServer

mcp = MCPServer("meal-helper")

@mcp.tool()
def get_meal_idea(ingredients: str, meal_type: str, goal: str) -> str:
    ingredients_lower = ingredients.lower()
    goal_lower = goal.lower()

    if "egg" in ingredients_lower and "paneer" in ingredients_lower:
        if "high-protein" in goal_lower:
            return f"For {meal_type}, try Paneer Egg Bhurji — a high-protein option."
    return f"For {meal_type}, try Paneer Egg Bhurji."

    if "rice" in ingredients_lower and "egg" in ingredients_lower:
        return f"For {meal_type}, try Egg Fried Rice."

    return f"For {meal_type}, you can make something using: {ingredients}"