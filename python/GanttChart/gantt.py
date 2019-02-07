import plotly.plotly as py
import plotly.figure_factory as ff


def get_GanttChart():
    #Seta as tarefas
    df = [dict(Task='PostgreSQL', Start='2019-01-23', Finish='2019-01-27', Resource='Lemos'),
          dict(Task='Python', Start='2019-02-02', Finish='2019-02-05', Resource='Cabral'),
          dict(Task='Scripts', Start='2019-01-27', Finish='2019-01-28', Resource='Breno'),
          dict(Task='Apresentação', Start='2019-01-31', Finish='2019-02-01', Resource='Camila')
    ]
    #Seta as cores 
    colors = dict(Lemos = 'rgb(54, 226, 31)',
                  Cabral = 'rgb(102, 24, 226)',
                  Breno = 'rgb(221, 247, 22)',
                  Camila = 'rgb(242, 7, 7)')
    #Cria o arquivo
    fig = ff.create_gantt(df,colors=colors, index_col='Resource', show_colorbar=True)
    py.iplot(fig, filename='gantt-dict-colors', world_reliable=True)

if __name__ == "__main__":
    
    get_GanttChart()