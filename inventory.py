import colors as Colors
import json
from selenium.webdriver.common.by import By


def equipment(driver):
    stats = None
    print("stats")
    print("1 - No")
    print("2 - Yes")
    stats_menu = input()
    match stats_menu:
        case "1":
            stats = False
        case "2":
            stats = True
    items_sum_number = 0
    items_buy_sum = 0
    items_sell_sum = 0
    unique_items = 0
    items = []
    types = ['animal', 'belt', 'body', 'pants', 'head', 'neck', 'foot', 'left_arm', 'right_arm', 'yield']
    for eq_type in types:
        bag = driver.execute_script(f"return Bag.items_by_type.{eq_type}")
        if bag is None:
            continue
        print(f'{Colors.blue}[INVENTORY]  **** {eq_type.upper()} ****')
        with open('twdump.json', encoding='utf-8') as f:
            json_data = json.load(f)
        for item_id in bag:
            for item in json_data.values():
                if str(item['item_id']) == item_id:
                    count = driver.execute_script(f"return Bag.getItemCount({item_id})")
                    items_buy_sum = items_buy_sum + (item["price"] * count)
                    items_sell_sum = items_sell_sum + (item["sell_price"] * count)
                    items_sum_number = items_sum_number + count
                    unique_items = unique_items + 1
                    print(
                        f'{Colors.blue}[INVENTORY]{Colors.magenta}[{unique_items}]'
                        f' {Colors.orange}ID:{Colors.green}{item_id} -'
                        f' "{item["name"]}" '
                        f'({Colors.orange}x{count}{Colors.green}){Colors.default} B: {item["price"]}$'
                        f' S: {item["sell_price"]}$')

                    if not stats:
                        continue
                    if not item["speed"] is None:
                        print(f'Speed: {item["speed"]}')
                    if not item["set"] is None:
                        print(f'({item["set"]})')
                    if item["sellable"]:
                        print("sellable")
                    if item["tradeable"]:
                        print("tradable")
                    if not item["usebonus"] is None:
                        print(item["usebonus"])
                    damage = item.get('damage')
                    if damage:
                        damage_min = damage.get('damage_min')
                        damage_max = damage.get('damage_max')
                        print(f"Item {item_id}: Damage min = {damage_min}, max = {damage_max}")
                    bonus = item.get('bonus')
                    if bonus:
                        for b in bonus.get('item', []):
                            desc = b.get('desc')
                            value = b.get('bonus', {}).get('value')
                            level = driver.find_element(By.CLASS_NAME, 'level').text
                            level = int(level)
                            calc_stats = level * value
                            calc_stats = round(calc_stats, 2)
                            print(f"{desc} | {calc_stats} at current level")

                    item_string = f'{item_id}: {item["name"]} (x{count}) \n'
                    items.append(item_string)
    print(f'{Colors.blue}[INVENTORY]{Colors.magenta}TOTAL ITEMS: {items_sum_number} | UNIQUE ITEMS {unique_items} '
          f'| BUY PRICE: {items_buy_sum}$ | SELL PRICE: {items_sell_sum}$')
