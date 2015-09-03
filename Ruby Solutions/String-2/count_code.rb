word = "codcodecore"

def count_code(string)
	count = 0
	for i in (0..string.length - 3)
		if string[i..i+1] == "co" and string[i+3] == "e"
			count += 1
		end
	end
	return count
end

p count_code(word)