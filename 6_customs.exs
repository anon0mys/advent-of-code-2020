defmodule Customs do
  def run do
    File.stream!("inputs/6_test_surveys.txt")
    |> Enum.map(&String.trim/1)
    |> Enum.chunk_while([], &chunk_func/2, &result/1)
    |> Enum.sum()
  end

  defp chunk_func("" = _line, group) do
    count = group
    |> List.flatten()
    |> Enum.uniq()
    |> Enum.count()
    {:cont, count, []}
  end

  defp chunk_func(line, group) do
    {:cont, [String.graphemes(line) | group]}
  end

  defp result(_last), do: {:cont, []}
end

Customs.run() |> IO.inspect
