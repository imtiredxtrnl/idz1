from analizer import TextAnalizator
from ResultModel import ResultModel
from dbcontext import Context


exclude = ["lorem","ipsum","penis"]
words = ["gayboy","рад","maxime"]
results = TextAnalizator.Analize("D://penis.pdf", words, exclude)
results.print_fields()
Context.create_table()
Context.insert_result(results)
