full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    """
    创建角色函数，包含完整的输入验证
    
    参数:
    name: 角色名称 (字符串)
    strength: 力量值 (整数)
    intelligence: 智力值 (整数)
    charisma: 魅力值 (整数)
    
    返回:
    如果验证通过：包含四行特定格式的字符串
    如果验证失败：错误信息字符串
    """
    # 验证名称是字符串类型
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    # 验证名称不是空字符串
    if name == '':
        return 'The character should have a name'
    
    # 验证名称长度不超过10
    if len(name) > 10:
        return 'The character name is too long'
    
    # 验证名称不包含空格
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    # 验证所有属性都是整数
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    
    # 验证所有属性不小于1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    
    # 验证所有属性不超过4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    
    # 验证所有属性的总和等于7
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    # 如果所有验证通过，构建四行字符串
    # 第一行：角色名称
    result = f"{name}\n"
    
    # 第二行：力量 (STR)
    result += f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
    
    # 第三行：智力 (INT)
    result += f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
    
    # 第四行：魅力 (CHA)
    result += f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    
    return result