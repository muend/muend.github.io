import re
from playwright.sync_api import Page, expect

def test_page_loads_and_has_correct_title(page: Page):
    page.goto("file:///app/index.html")
    expect(page).to_have_title(re.compile("Batı Antalya Tarımsal Kalkınma Rehberi"))

def test_form_interaction_and_results_display(page: Page):
    page.goto("file:///app/index.html")

    ilce_select = page.locator("#ilceSelect")
    mahalle_select = page.locator("#mahalleSelect")
    hesapla_button = page.locator("#hesaplaButton")
    results_area = page.locator("#resultsArea")
    bolge_title = page.locator("#bolgeTitle")
    crops_table_body = page.locator("#cropsTableBody")
    long_term_recommendation = page.locator("#longTermRecommendation")
    market_gap_text = page.locator("#marketGapText")

    expect(mahalle_select).to_be_disabled()
    expect(hesapla_button).to_be_disabled()

    ilce_select.select_option("Finike")

    expect(mahalle_select).to_be_enabled()
    expect(hesapla_button).to_be_disabled()

    mahalle_select.select_option("Turunçova")

    expect(hesapla_button).to_be_enabled()

    hesapla_button.click()

    expect(results_area).to_be_visible()
    expect(bolge_title).to_have_text("Analiz Sonuçları: Turunçova, Finike")

    expect(crops_table_body).to_contain_text("Domates (Sera)")
    expect(long_term_recommendation).to_contain_text("Portakal (Finike - Coğrafi İşaretli)")
    expect(market_gap_text).to_contain_text("Avokado, Narenciye Arası Sera Sebzeciliği")

def test_print_button_is_visible_and_functional(page: Page):
    page.goto("file:///app/index.html")

    ilce_select = page.locator("#ilceSelect")
    mahalle_select = page.locator("#mahalleSelect")
    hesapla_button = page.locator("#hesaplaButton")
    print_button = page.locator("#printButton")

    ilce_select.select_option("Kumluca")
    mahalle_select.select_option("Mavikent")
    hesapla_button.click()

    expect(print_button).to_be_visible()
