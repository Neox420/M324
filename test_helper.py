def test_sort(): 

    # Given: I have several to-dos with dates 

    todos = [("Universum debuggen", "2023-09-06"), 

             ("Sinn des Lebens entdecken", "2023-09-01"), 

             ("Superheld werden", "2023-10-25"), 

             ("Netto null", "2050-01-01")] 

 

    # When: I add the items 

    for todo in todos: 

        helper.add(todo[0], todo[1]) 

 

    # Then: They should be sorted by date 

    for i in range(len(helper.items) - 1): 

        assert helper.items[i].date < helper.items[i+1].date 